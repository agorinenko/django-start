from envparse import env

from web_app.settings._redis import REDIS_CONNECTION_STRING

ENV_TYPE = env.str('ENV')
KEY_PREFIX = env.str('KEY_PREFIX', default='web_app0')
USE_DUMMY_CACHE = env.bool('USE_DUMMY_CACHE', default=False)

if USE_DUMMY_CACHE:
    cache_info = {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
else:
    cache_info = {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_CONNECTION_STRING,
        'KEY_PREFIX': KEY_PREFIX,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_KWARGS': {
                'max_connections': 50,  # Ограничить пул соединений
                'timeout': 10,  # Таймаут ожидания соединения
                'retry_on_timeout': True,  # Повтор при таймауте
            },
            'SOCKET_CONNECT_TIMEOUT': 30,  # Таймаут подключения
            'SOCKET_TIMEOUT': 10,  # Таймаут операций
            'HEALTH_CHECK_INTERVAL': 15,  # Проверка здоровья каждые 15 сек
            'MAX_RETRIES': None,  # Количество попыток
            'RETRY_DELAY': 1,  # Задержка между попытками
            'RETRY_ON_TIMEOUT': True,
            'IGNORE_EXCEPTIONS': False,  # Не игнорировать исключения
        }
    }

CACHES = {
    'default': cache_info
}
