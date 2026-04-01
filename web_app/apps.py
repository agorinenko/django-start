# pylint: disable=all
from django.apps import AppConfig


class WebAppConfig(AppConfig):
    """ Основное веб-приложение """

    name = "web_app"
    verbose_name = "Веб приложение"

    def ready(self):
        try:
            super().ready()
            from web_app import tasks
            from web_app.signals import signals_connect

            signals_connect()
        except ImportError:
            pass
