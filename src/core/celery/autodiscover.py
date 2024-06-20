from src.core.celery import celery


tasks = [
    'src.v1.pictures',
]


celery.autodiscover_tasks(tasks)
