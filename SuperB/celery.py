import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperB.settings")
app = Celery("SuperB")
app.conf.enable_utc=False
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# celery -A SuperB beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
# celery -A SuperB worker --pool=solo -l info