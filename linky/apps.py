from django.apps import AppConfig


class LinkyConfig(AppConfig):
    name = 'linky'
    def ready(self):
        import linky.signals
