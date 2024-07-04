from io import BytesIO
from pprint import pprint

from PIL import Image

from src.core.storages.manager import storage_manager
from src.v1.pictures.repositories.db_grud import PictureRepository
from src.v1.pictures.repositories.storage_grud import StorageRepository
from src.v1.pictures.services.pictures import PictureService

from src.core.database import db_manager
from src.v1.pictures.services.storages import StorageService
from src.v1.pictures.utils.pictures import get_path

from src.v1.pictures.workers.celery import celery


@celery.task
async def task_add_picture_versions_to_storage(pk: int):

    storage = StorageService(StorageRepository(storage_manager))

    async with db_manager.session() as session:
        picture = PictureService(PictureRepository(session))

    instance = await picture.get_by_id(pk)

    print('*******', instance)

    response = await storage.get_original_file(instance)
    image_data = response.read()

    print('-------', response.data)
    print('+++++++++', response.info())
    # print('+++++++++', image_data)

    image = Image.open(BytesIO(image_data))

    print(image.size, image.info)

    if instance:
        print(instance)

