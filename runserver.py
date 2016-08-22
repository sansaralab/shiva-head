from shiva.common import settings
from shiva import app


app.run(port=settings.APP_PORT, host=settings.APP_HOST, debug=settings.APP_DEBUG)
