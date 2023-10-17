import typing

import fastapi.security
import httpx


class BearerAuth(httpx.Auth):
    def __init__(
            self, token: fastapi.security.HTTPAuthorizationCredentials, /
    ) -> None:
        self._auth_header = r' '.join([token.scheme, token.credentials])

    def auth_flow(
            self, request: fastapi.Request
    ) -> typing.Generator[fastapi.Request, fastapi.Response, None]:
        request.headers["Authorization"] = self._auth_header
        yield request

    def __str__(self):
        return self._auth_header
