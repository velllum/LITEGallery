from celery import Celery


celery = Celery(__name__)
celery.config_from_object('core.configs', namespace='CELERY')






