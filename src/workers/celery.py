from celery import Celery

from src.workers.beat import beat_schedule

celery = Celery(__name__)
celery.config_from_object('src.workers.config')
celery.autodiscover_tasks(['src.workers.tasks'])
celery.conf.beat_schedule = beat_schedule

