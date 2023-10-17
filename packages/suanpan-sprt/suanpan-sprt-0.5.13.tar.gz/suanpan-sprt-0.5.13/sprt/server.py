import re
import json
import logging
import typing
import pathlib
import dataclasses
import pydantic
from contextlib import redirect_stdout, redirect_stderr, contextmanager
from quart import Quart
from quart_schema import QuartSchema, validate_request, validate_response, RequestSchemaValidationError
from quart_schema import validation
from . import loader, envs, exceptions, utils


@dataclasses.dataclass
class FunctionContext:
    request_id: str
    node_id: str
    # 右面板参数
    params: typing.Optional[dict]
    # 输入桩参数
    args: dict


@dataclasses.dataclass
class FunctionParams:
    id: str
    file: str
    working_dir: typing.Optional[str]
    context: FunctionContext
    function: typing.Optional[str] = "main"


@dataclasses.dataclass
class FunctionResponse:
    id: str
    success: bool
    error: typing.Optional[str] = None
    data: typing.Optional[dict] = None


def acquire_resource(node_id):
    envs.nodeId = node_id
    return node_id


def release_resource(ctx):
    envs.nodeId = None


@contextmanager
def node_context(*args, **kwargs):
    resource = acquire_resource(*args, **kwargs)
    try:
        yield resource
    finally:
        release_resource(resource)


def create_app(working_dir='.', log_file='', new_log=False):
    log_path = pathlib.Path(log_file).parent
    filename = pathlib.Path(log_file).name
    logfile_prefix = filename.split('-')[0:2]
    app = Quart(__name__)
    QuartSchema(app)

    @app.post("/")
    @validate_request(FunctionParams)
    @validate_response(FunctionResponse)
    async def handle_post(data: FunctionParams) -> FunctionResponse:
        node_id = data.context.node_id
        if new_log:
            log_dir = log_path / f'{logfile_prefix[0]}-{logfile_prefix[1]}-{node_id}'
            log_dir.mkdir(parents=True, exist_ok=True)
            log_name = log_dir / f'app-{logfile_prefix[0]}-{node_id}'
        else:
            log_name = log_path / node_id
        if utils.should_log_rollover(str(log_name)):
            utils.do_log_rollover(str(log_name))
        with open(log_name, 'a', encoding='utf8') as f:
            with redirect_stdout(f), redirect_stderr(f), node_context(node_id):
                function = None
                try:
                    logging.debug(f'event: {data.context.args}')
                    function = load(data, working_dir)
                    ret = await function.call_func(data.context.request_id, data.context.args, data.context.params)
                    logging.debug(f'response: {ret}')
                    out_data = {key: value for key, value in ret.items() if
                                re.match(r"out\d+", key) and value is not None}
                    resp = FunctionResponse(id=data.id, success=True, data=out_data)
                except Exception as e:
                    if function is not None:
                        function.context.log.exception(f'event error: {e}')
                    else:
                        logging.exception(f'event error: {e}')
                    resp = FunctionResponse(id=data.id, success=False, error=str(e))

        return resp

    @app.errorhandler(RequestSchemaValidationError)
    async def handle_request_validation_error(error):
        if isinstance(error.validation_error, TypeError):
            err = str(error.validation_error)
        else:
            err = error.validation_error.json()

        return {"errors": err}, 400

    @app.get("/health/liveness")
    async def liveness():
        return "OK"

    @app.get("/health/readiness")
    async def readiness():
        return "OK"

    return app


module_imported = {}


def load(data: FunctionParams, default_dir):
    node_id = data.context.node_id
    working_dir = data.working_dir if data.working_dir else default_dir
    filename = data.file
    function = data.function

    node_function = module_imported.get(node_id)
    if not node_function:
        logging.info(f'node {node_id} import function {function} from {filename}')
        node_function = loader.NodeFunction(node_id, working_dir, filename, function)
        module_imported[node_id] = node_function

    return node_function


async def handle_event(event_data, working_dir='.'):
    model_class = validation._to_pydantic_model(FunctionParams)
    try:
        json_data = json.loads(event_data)
        data = model_class(**json_data)
        data = typing.cast(FunctionParams, data)
    except (json.decoder.JSONDecodeError, TypeError, pydantic.ValidationError) as error:
        logging.exception(f'event error: {error}')
        raise exceptions.RequestSchemaValidationError(error)

    function = None
    try:
        logging.debug(f'event: {data.context.args}')
        function = load(data, working_dir)
        ret = await function.call_func(data.context.request_id, data.context.args, data.context.params)
        logging.debug(f'response: {ret}')
        out_data = {key: value for key, value in ret.items() if re.match(r"out\d+", key)}
        resp = FunctionResponse(id=data.id, success=True, data=out_data)
    except Exception as e:
        if function is not None:
            function.context.log.exception(f'event error: {e}')
        else:
            logging.exception(f'event error: {e}')
        resp = FunctionResponse(id=data.id, success=False, error=str(e))

    return resp
