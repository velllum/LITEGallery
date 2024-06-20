from celery import Celery

from src.core.configs import settings


# celery = Celery(__name__)
# celery.config_from_object('src.core.configs', namespace='CELERY')

tasks = [
    'pictures',
]

celery = Celery(
    __name__,
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
    include=tasks,
)




