from pprint import pprint

from src.core.storages.manager import storage_manager
from src.v1.pictures.repositories.db_grud import PictureRepository
from src.v1.pictures.repositories.storage_grud import StorageRepository
from src.v1.pictures.services.pictures import PictureService

from src.core.database import db_manager
from src.v1.pictures.services.storages import StorageService
from src.v1.pictures.utils.pictures import get_path

from src.v1.pictures.workers.celery import celery


@celery.task
async def task_add_picture_versions_to_storage(pk: int, project_id: int):

    storage = StorageService(StorageRepository(storage_manager))

    async with db_manager.session() as session:
        picture = PictureService(PictureRepository(session))

    instance = await picture.get_by_id(pk)

    pprint(await storage.get_file_all([instance]))

    print('Hello world')
    print(instance.project_id)

    if instance:
        print(instance)


