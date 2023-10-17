from nicegui import app

import forta.auth.core
import forta.fastapi
import forta.lk.core
import forta.odata.core
import forta.payout.core

(app.redoc_url,
 app.docs_url,
 app.openapi_url,
 app.swagger_ui_oauth2_redirect_url) = [app.remove_route(path=_) for _ in [app.redoc_url, app.docs_url, app.openapi_url,
                                                                           app.swagger_ui_oauth2_redirect_url, r'/']][:4]

app.mount(path=f'/auth',
          app=forta.auth.core.app,
          name=forta.auth.core.app.title)

app.mount(path=f'/odata',
          app=forta.odata.core.app,
          name=forta.odata.core.app.title)

app.mount(path=f'/payout',
          app=forta.payout.core.app,
          name=forta.payout.core.app.title)

app.mount(path=f'/lk',
          app=forta.lk.core.app,
          name=forta.lk.core.app.title)
