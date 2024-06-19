from celery import Celery

from src.core.configs import settings


# celery = Celery(__name__)
# celery.conf.broker_url = settings.REDIS_URL
# celery.conf.result_backend = settings.REDIS_URL

celery = Celery('tasks', broker=settings.REDIS_URL)

