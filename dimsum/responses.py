from json import dumps
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from starlette.responses import Response, JSONResponse, PlainTextResponse, RedirectResponse


def _encode_json(o):
    if isinstance(o, BaseModel):
        return jsonable_encoder(o)
    return dumps(o)


def json(model):
    encoded = _encode_json(model)
    return JSONResponse(content=encoded)


def text(content):
    return PlainTextResponse(content)


def not_found(content=None, json_content=True):
    encoded = _encode_json(content) if json_content else content
    return Response(content=encoded, status_code=404)


def redirect(location, temporary=True):
    code = 307 if temporary else 301
    return RedirectResponse(location, status_code=code)


def not_modified():
    return Response(status_code=304)