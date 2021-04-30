from envparse import env

CORS_ALLOWED_ORIGINS_STR = env.str("CORS_ALLOWED_ORIGINS", default=None)
CORS_ALLOWED_ORIGINS = [v for v in CORS_ALLOWED_ORIGINS_STR.split(",") if v] if CORS_ALLOWED_ORIGINS_STR else []
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS", default=False)
CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS", default=False)
