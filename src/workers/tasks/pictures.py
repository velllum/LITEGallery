from sqlalchemy.orm import Session

from src.core.database.db_sync import get_session
from src.v1.pictures import models
from src.workers.celery import celery


@celery.task
def task_add_picture_versions_to_storage(pk: int, project_pk: int, session: Session = get_session()):
    """- сгенерировать и добавить версии картинки в хранилище """
    print(pk, project_pk)
    # instance = db.get(Picture, pk)
    # with session.begin():
    db = get_session()
    instance = db.query(models.Picture).filter(models.Picture.id == pk).first()
    # instance = session.query(Picture).get(36)

    print(instance)

    if instance:
        print(instance)


