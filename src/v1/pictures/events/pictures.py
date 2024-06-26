from pprint import pprint

from sqlalchemy import event

from src.v1.pictures.models import Picture
from src.workers.tasks.pictures import task_add_picture_versions_to_storage


@event.listens_for(Picture, 'after_insert')
def event_add_picture_versions_to_storage(mapper, connection, target):
    """- сгенерировать и добавить версии картинки в хранилище """
    print(mapper, connection, target)

    pprint("******* event_add_picture_versions_to_storage")
    task_add_picture_versions_to_storage.delay(target.id, target.project_id)

