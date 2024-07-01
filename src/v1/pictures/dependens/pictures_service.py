from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_db
from src.core.storages.manager import storage_manager
from src.v1.pictures.repositories.db_grud import PictureRepository
from src.v1.pictures.repositories.storage_grud import StorageRepository
from src.v1.pictures.services import PictureService, StorageService

async_db = Depends(get_async_db)


async def get_picture_service(db: AsyncSession = async_db) -> PictureService:
    """- Зависимость между сервисом картинки и репозиторием с GRUD оперениями БД """
    return PictureService(PictureRepository(db))


async def get_storage_service() -> StorageService:
    """- Зависимость между сервисом файлового хранилища и репозиторием с GRUD оперениями хранилища """
    return StorageService(StorageRepository(storage_manager))


picture_service = Annotated[PictureService, Depends(get_picture_service)]
storage_service = Annotated[StorageService, Depends(get_storage_service)]

