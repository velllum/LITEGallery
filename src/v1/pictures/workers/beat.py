from celery.schedules import crontab


beat_schedule = {
    'add-30-seconds': {
        'task': 'src.workers.tasks.pictures.add_to_storage',
        'schedule': 30.0,
        # 'args': (16, 16)
    },
    # 'everyday-task': {
    #   'task': 'src.workers.tasks',
    #   'schedule': crontab(hour='7', minute='0')
    # }
}


