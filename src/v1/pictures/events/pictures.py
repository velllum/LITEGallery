from sqlalchemy import event
from sqlalchemy.orm import Session

from src.workers.tasks.pictures import task_add_picture_versions_to_storage


@event.listens_for(Session, "after_flush")
def receive_after_flush(session, flush_context):
    print('***********', session.new, session.dirty, session.info, flush_context)
    _object, = session.new
    session.info.update(**{'pk': _object.id, 'project_id': _object.project_id})


@event.listens_for(Session, "after_commit")
def receive_after_commit(session):
    pk = session.info.get('pk')
    project_id = session.info.get('project_id')
    task_add_picture_versions_to_storage(pk, project_id)
    # task_add_picture_versions_to_storage.delay(**session.info.get('after_flush'))

