from envparse import env

use_db_pool = env.bool('DB_POOL', default=False)
# https://www.psycopg.org/psycopg3/docs/api/pool.html#psycopg_pool.ConnectionPool
base_config = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env.str("POSTGRES_DB"),
    'USER': env.str("POSTGRES_USER"),
    'PASSWORD': env.str("POSTGRES_PASSWORD"),
    'HOST': env.str("DB_HOST"),
    'PORT': env.int("DB_PORT"),
    'CONN_MAX_AGE': env.int('CONN_MAX_AGE', default=0),
    'CONN_HEALTH_CHECKS': env.bool('CONN_HEALTH_CHECKS', default=False)
}
if use_db_pool:
    base_config.update({
        'OPTIONS': {
            'pool': {
                'min_size': env.int('DB_POOL_MIN_SIZE', default=4),
                'max_size': env.int('DB_POOL_MAX_SIZE', default=10),
                'max_lifetime': env.int('DB_POOL_LIFETIME', default=3600),  # 1 hour
                'max_idle': env.int('DB_POOL_MAX_IDLE', default=600),  # 10 minutes
                'timeout': env.int('DB_POOL_TIMEOUT', default=30),  # 30 second
                'num_workers': env.int('DB_POOL_WORKERS', default=3),
            }
        }
    })

DATABASES = {
    'default': base_config
}
