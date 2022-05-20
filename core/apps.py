from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    # verbose_name is the name that is displayed in Django Admin
    verbose_name = 'HOV'
