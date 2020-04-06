from .base import *
from envparse import env

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = [
    # Example
    # ".subsite.site.ru",
    # ".subsite.site.ru.",
]
