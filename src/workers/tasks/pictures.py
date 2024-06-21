from src.workers.celery import celery


@celery.task
def add_to_storage():
    """- добавить данные в хранилище """
    # TODO: здесь должен быть сервис который добавить в хранилище
    #  данные и передаст запись в базу данных
    print('Hello world!!!')


