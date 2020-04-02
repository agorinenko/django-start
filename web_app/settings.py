import os

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv
from envparse import env

load_dotenv()

ENV_TYPE = env.str('APP_ENV')

if ENV_TYPE == "DEV":
    print("Warning! Server started in DEVELOPMENT mode. Use APP_ENV variable with values: PROD, TEST, DEV")
    from web_app.var_settings.development import *
elif ENV_TYPE == "TEST":
    from web_app.var_settings.test import *
elif ENV_TYPE == "PROD":
    from web_app.var_settings.production import *
else:
    raise ImproperlyConfigured(f"Not implemented error: ENV_TYPE={ENV_TYPE}")
