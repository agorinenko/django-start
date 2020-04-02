from .base import *
from envparse import env

DEBUG = env.str('DEBUG')

ALLOWED_HOSTS = [
    # Example
    # ".subsite.site.ru",
    # ".subsite.site.ru.",
]
