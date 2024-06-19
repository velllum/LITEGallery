from src.v1.pictures.tasks import celery


@celery.task
def task_add():
    """- добавить новое изображение """
    # TODO: здесь должен быть сервис который добавить в хранилище
    #  данные и передаст запись в базу данных

