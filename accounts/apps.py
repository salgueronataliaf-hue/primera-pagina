# accounts/apps.py

from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # ESTA FUNCIÓN CONECTA LAS SEÑALES
    def ready(self):
        import accounts.signals