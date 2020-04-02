from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1'
)

CSRF_TRUSTED_ORIGINS = [
]
CSRF_COOKIE_SAMESITE = None
CSRF_COOKIE_SECURE = False

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
]
CORS_ALLOW_CREDENTIALS = True

SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_AGE = 1209600  # 2 недели

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
# 25 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440 * 10