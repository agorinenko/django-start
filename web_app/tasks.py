import logging
import pprint
from collections.abc import Callable

from billiard.exceptions import SoftTimeLimitExceeded

from django import db
from django.conf import settings

logger = logging.getLogger(__name__)


def _common_task(task, task_function: Callable, *args, cleanup_function: Callable | None = None, **kwargs):
    if args and args[0] is None:
        args = list(args)
        args.pop(0)

    logger.debug("================ START TASK %s ================\nargs: %s\nkwargs: %s", task.name,
                 pprint.pformat(args), pprint.pformat(kwargs))
    if not settings.CELERY_EAGER:
        _check_connections()
    try:

        return task_function(*args, **kwargs)
    except SoftTimeLimitExceeded:
        logger.info('Soft time limit exceeded in %s.', task.name)
        if cleanup_function:
            cleanup_function()

        return {
            'exception': 'soft_time_limit_exceeded'
        }
    except Exception as ex:  # pylint: disable=broad-except
        logger.exception(ex)

        return {
            'exception': str(ex)
        }
    finally:
        if not settings.CELERY_EAGER:
            db.close_old_connections()
        logger.debug("================ END TASK %s ================", task.name)


def _check_connections():
    """ Проверка соединений с Django """
    for conn in db.connections.all():
        try:
            cur = conn.cursor()
            _ = cur.execute('SELECT pg_backend_pid()')
        except (db.OperationalError, db.InterfaceError):
            conn.close()
