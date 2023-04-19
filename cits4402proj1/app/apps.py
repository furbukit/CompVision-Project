# This file defines the configuration for the app itself, such as the app name, label, and verbose name. 
# You can also use this file to define app-level settings and signals.
from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
