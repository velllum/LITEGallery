# from typing import Annotated
#
# from fastapi.params import Depends
# from sqlalchemy.orm import Session
# from src.core.database.db_sync import get_session
# from src.v1.pictures import models
# from src.v1.pictures.dependens.pictures_service import picture_service, storage_service
# from src.v1.pictures.services import PictureService, StorageService
# from src.v1.pictures.dependens.pictures_service import get_picture_service, get_storage_service
# from src.workers.celery import celery
#
# picture_service = get_picture_service()
# storage_service = get_storage_service()
#
# @celery.task
# # def task_add_picture_versions_to_storage(pk: int, project_id: int, session: Session = get_session()):
# def task_add_picture_versions_to_storage(pk: int, project_id: int,
#                                          picture: picture_service,
#                                          storage: storage_service):
#     """- сгенерировать и добавить версии картинки в хранилище """
#     # instance = session.get(models.Picture, pk)
#     instance = picture.get_by_id(pk)
#     # instance = session.query(models.Picture).filter(models.Picture.id == pk).first()
#
#     print(instance)
#
#     if instance:
#         print(instance)


