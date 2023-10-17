import fastapi

import forta.fastapi

app = forta.fastapi.fabric(redoc_url=None, docs_url=None, openapi_url=None,
                           swagger_ui_oauth2_redirect_url=None, title=r'oData',
                           middleware=[forta.fastapi.cors])


@app.get(path=r'/processing', include_in_schema=False,
         response_class=fastapi.responses.PlainTextResponse)
async def request(request: fastapi.Request, response: fastapi.Response) -> str:
    return 'response'
