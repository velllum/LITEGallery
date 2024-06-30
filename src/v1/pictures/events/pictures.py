from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from src.core.database import get_async_db, db_manager, get_session, Base
from src.v1.pictures.models import Picture
from src.v1.pictures.utils.pictures import get_path
from src.workers.tasks.pictures import task_add_picture_versions_to_storage


# sync_session: Session = get_session()
async_session: AsyncSession = db_manager.session()
# async with db_manager.session() as async_session:
#     async with async_session.begin():
#         _session = async_session



@event.listens_for(AsyncSession, 'after_flush_handler')
def receive_afterpopo_flush(session, flush_context):
    print('654654564654', session, flush_context)


# @event.listens_for(Base, 'after_insert')
@event.listens_for(Picture, 'after_insert')
# @event.listens_for(Picture, 'after_commit')
def event_add_picture_versions_to_storage(mapper, connection, target):
    """- сгенерировать и добавить версии картинки в хранилище """

    print("******* event_add_picture_versions_to_storage")

    print(mapper, connection, target, target.id)

    # task_add_picture_versions_to_storage.delay(target.id)
    task_add_picture_versions_to_storage(target.id, target.project_id)

