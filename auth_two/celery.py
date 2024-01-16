import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auth_two.settings")

app = Celery("auth_two")
app.config_from_object("auth_two.celeryconfig")
app.autodiscover_tasks()