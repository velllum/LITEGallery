import asyncio

from sqlalchemy import event
from sqlalchemy.orm import Session


@event.listens_for(Session, "after_flush")
def receive_after_flush(session, flush_context):
    print('***********', session.new, session.dirty, session.info, flush_context)
    _object, = session.new
    session.info.update(**{'pk': _object.id})


@event.listens_for(Session, "after_commit")
def receive_after_commit(session):
    pk = session.info.get('pk')

    from src.v1.pictures.workers import tasks

    loop = asyncio.get_event_loop()
    loop.create_task(tasks.task_add_picture_versions_to_storage(pk))
    # task_add_picture_versions_to_storage.delay(pk)

