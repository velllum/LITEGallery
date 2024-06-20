from celery.schedules import crontab

from src.core.celery import celery


celery.conf.beat_schedule = {
    # 'run-me-every-ten-seconds': {
    #     'task': 'checker.tasks.check',
    #     'schedule': 10.0
    # }
}

# celery.conf.beat_schedule = {
#     'everyday-task': {
#       'task': 'checker.tasks.remember_tasks_to_do',
#       'schedule': crontab(hour='7', minute='0')
#     }
# }