import os
from pathlib import Path

from envparse import env

LOG_LEVEL = env.str('LOGGING_DEFAULT_LEVEL')
LOGGING_DEFAULT_HANDLER = env.str('LOGGING_DEFAULT_HANDLER', default='console')
ENV_TYPE = env.str('ENV')

LOG_DIR = os.path.join(Path(__file__).parents[2], "log")
Path(LOG_DIR).mkdir(parents=True, exist_ok=True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'default': {
            'format': '%(levelname)s %(name)s %(asctime)s %(module)s %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'filename': f'{LOG_DIR}/{ENV_TYPE}.log',
            'formatter': 'default',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        },
        'null': {
            "class": 'logging.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['null', ],
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        'django.db.backends': {
            'level': 'DEBUG',
        },
        '': {
            'handlers': [LOGGING_DEFAULT_HANDLER],
            'level': LOG_LEVEL,
        }
    }
}
