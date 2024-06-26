from src.workers.celery import celery


@celery.task
def task_add_picture_versions_to_storage(id: int, project_id: int):
    """- сгенерировать и добавить версии картинки в хранилище """
    print('****** Hello world!!!')
    print(id, project_id)


