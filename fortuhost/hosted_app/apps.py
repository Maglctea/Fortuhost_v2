from django.apps import AppConfig


class HostedAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hosted_app'
    verbose_name = 'Приложения'
