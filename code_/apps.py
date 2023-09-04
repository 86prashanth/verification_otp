from django.apps import AppConfig


class CodeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'code_'


    def ready(self):
        import code_.signals