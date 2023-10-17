from django.conf import settings
from celery import Celery


def create_app(project_name: str) -> Celery:
    app: Celery = Celery(project_name, backend=settings.CELERY_BROKER_URL)
    app.config_from_object('django.config:settings', namespace='CELERY')
    app.autodiscover_tasks()
    return app
