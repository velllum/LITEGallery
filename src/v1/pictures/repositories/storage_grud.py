import io
from abc import ABC, abstractmethod

from typing import Type, Sequence, Any

from fastapi import HTTPException, UploadFile
from minio.helpers import ObjectWriteResult
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.configs import settings
from src.core.storages.manager import StorageManager


class AbstractRepository(ABC):

    @abstractmethod
    async def add(self, *args, **kwargs) -> None:
        """- создать """
        raise NotImplementedError

    @abstractmethod
    async def get_all(self, *args, **kwargs) -> None:
        """- получить список """
        raise NotImplementedError


class Repository(AbstractRepository):

    def __init__(self, db: AsyncSession, storage_manager: StorageManager):
        self.__db = db
        self.__storage = storage_manager

    async def add(self, file: UploadFile, instance_id: int, project_id: int) -> ObjectWriteResult:
        """- добавить """
        instance = self.__storage.client.put_object(
            bucket_name=settings.MINIO_CLIENT_NAME_BUCKETS,
            object_name=f"{project_id}/{instance_id}/{file.filename}",
            data=io.BytesIO(file.file.read()),
            content_type=file.content_type,
            length=file.size
        )
        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ОШИБКА ДОБАВЛЕНИЯ В ХРАНИЛИЩА')
        return instance

    async def get_all(self, project_id: int, skip: int = 0, limit: int = 100) -> Sequence[Any]:
        """- получить список """
        # TODO: Описать получение всех файлов из хранилища по указанному id проекта project_id
        # instance = await self.db.execute(select(self.model).offset(skip).limit(limit))
        # return instance.scalars().all()


class StorageRepository(Repository):
    ...
