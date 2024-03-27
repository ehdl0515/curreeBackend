from django.apps import AppConfig

from curreeBackend_config import settings


class CurreeBackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'curreeBackend'
