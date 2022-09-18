from django.apps import AppConfig


# https://docs.djangoproject.com/en/4.1/ref/applications/#django.apps.AppConfig.label
class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
