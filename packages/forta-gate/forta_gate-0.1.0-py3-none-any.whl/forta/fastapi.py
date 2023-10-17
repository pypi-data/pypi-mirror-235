import functools
import pathlib
import typing

import fastapi.middleware.cors

redoc_path = pathlib.PurePosixPath(r'/')
docs_path = pathlib.PurePosixPath(r'/swagger')

cors = fastapi.middleware.Middleware(
        fastapi.middleware.cors.CORSMiddleware,
        allow_credentials=True,
        allow_origins=[r'*'],
        allow_methods=[r'*'],
        allow_headers=[r'*'])

fabric = typing.Annotated[
    fastapi.FastAPI,
    functools.partial(fastapi.FastAPI,
                      redoc_url=str(redoc_path),
                      docs_url=str(docs_path),
                      swagger_ui_oauth2_redirect_url=None,
                      middleware=[cors])]
