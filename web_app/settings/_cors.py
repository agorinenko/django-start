from envparse import env

from web_app.settings.utils import parse_str_to_list

ENV_CORS_ALLOWED_ORIGINS = env.str("CORS_ALLOWED_ORIGINS", default=None)
CORS_ALLOWED_ORIGINS = parse_str_to_list(ENV_CORS_ALLOWED_ORIGINS, default=[])
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS", default=False)
CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS", default=False)
