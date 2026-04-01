def signals_connect():
    """Connect to signals."""
    from django.db.models import signals

    # signals.post_save.connect(
    #     f_signal, sender=models.TaskWhiteList, weak=False,
    #     dispatch_uid='post_save__TaskWhiteList__f_signal'
    # )
    # signals.post_delete.connect(
    #     f_signal, sender=models.TaskWhiteList, weak=False,
    #     dispatch_uid='post_delete__TaskWhiteList__f_signal'
    # )


def f_signal(*args, **kwargs):
    """ Сигнал """
    from celery_misc.celery_monitoring.monitoring_utils import TASK_REPOSITORY

    TASK_REPOSITORY.refresh_state()
