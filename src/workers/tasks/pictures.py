from src.workers.celery import celery


@celery.task
def task_add_picture_versions_to_storage(id: int, project_id: int, filename: str):
    """- сгенерировать и добавить версии картинки в хранилище """
    print('****** Hello world!!!')


