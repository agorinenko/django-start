import logging
from celery_misc import celery_utils

from web_app.celery import app

logger = logging.getLogger(__name__)


@app.task(bind=True, max_retries=5, retry_backoff=3, retry_backoff_max=600, retry_jitter=True)
def send_events_only_ones(self, *args, **kwargs):
    """ Однократная отсылка созданных событий """
    return celery_utils.common_celery_task(self, _send_events, *args, **kwargs)


@app.task(bind=True)
def send_events(self, *args, **kwargs):
    """ Периодическая отсылка не отправленных сообщений """
    return celery_utils.safety_celery_task(self, _send_events, *args, suppress_events_error=True, **kwargs)


def _send_events(_, *args, **kwargs):
    pass
