from web_app.var_settings._redis import REDIS_HOST, REDIS_PORT

ASGI_APPLICATION = 'web_app.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": ['redis://' + REDIS_HOST + ':' + REDIS_PORT + '/2'],
        },
    },
}
