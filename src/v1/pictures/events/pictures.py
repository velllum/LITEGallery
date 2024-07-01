from sqlalchemy import event
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session

from src.core.configs import settings
from src.core.database import get_async_db, db_manager, get_session, Base
from src.v1.pictures.models import Picture
from src.v1.pictures.utils.pictures import get_path
from src.workers.tasks.pictures import task_add_picture_versions_to_storage


# # sync_session: Session = get_session()
# async_session: AsyncSession = get_async_db()
# # async with db_manager.session() as async_session:
# #     async with async_session.begin():
# #         _session = async_session
#
# it = get_async_db()
# it.__anext__()

# print('*** *async_session', async_session, anext(async_session), type(async_session))


# session = AsyncSession(db_manager._engine)
#
#
@event.listens_for(Session, "after_flush")
def receive_afterpopo_flush(session, flush_context):
    print("after flush!")
    session: Session = session
    print('***********', session.new, session.dirty, session.info, flush_context)
    _object, = session.new
    session.info.update(**{'pk': _object.id, 'project_id': _object.project_id})
    print(session.info)
    print('----------------------------------------')

# event.listen(it.sync_session, "after_flush", receive_afterpopo_flush)

@event.listens_for(Session, "after_commit")
def my_after_commit(session):
    print("after commit!")
    session: Session = session
    print(session.new, session.dirty)
    print(session.info)
    pk = session.info.get('pk')
    project_id = session.info.get('project_id')
    # print("******* my_after_commit")
    # o, = session.new
    # # task_add_picture_versions_to_storage.delay(target.id)
    task_add_picture_versions_to_storage(pk, project_id)
    print('----------------------------------------')


# # @event.listens_for(Base, 'after_insert')
# @event.listens_for(Picture, 'after_insert')
# # @event.listens_for(Picture, 'after_commit')
# def event_add_picture_versions_to_storage(mapper, connection, target):
#     """- сгенерировать и добавить версии картинки в хранилище """
#
#     print("******* event_add_picture_versions_to_storage")
#
#     print(mapper, connection, target, target.id)
#
#     # task_add_picture_versions_to_storage.delay(target.id)
#     task_add_picture_versions_to_storage(target.id, target.project_id)

