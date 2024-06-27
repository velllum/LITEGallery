import io
from abc import ABC, abstractmethod

from typing import Type, Sequence, Any

from fastapi import HTTPException, UploadFile
from minio.helpers import ObjectWriteResult
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.configs import settings
from src.core.storages.manager import StorageManager
from src.v1.pictures.models import Picture
from src.v1.pictures.utils.pictures import get_full_path, get_path


class AbstractRepository(ABC):

    @abstractmethod
    async def add(self, *args, **kwargs) -> None:
        """- создать """
        raise NotImplementedError

    @abstractmethod
    async def get_by_id_all(self, *args, **kwargs) -> None:
        """- получить список """
        raise NotImplementedError


class Repository(AbstractRepository):

    def __init__(self, storage_manager: StorageManager):
        self.__storage = storage_manager
        self.__object = None

    async def add(self, file: UploadFile, instance: Type | Picture):
        """- добавить """
        self.__object = self.__storage.client.put_object(
            bucket_name=self.__storage.get_bucket(settings.MINIO_CLIENT_NAME_BUCKETS),
            object_name=await get_full_path(instance, 'original', file.filename),
            data=io.BytesIO(file.file.read()),
            content_type=file.content_type,
            length=file.size
        )
        if not self.__object:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ОШИБКА ДОБАВЛЕНИЯ В ХРАНИЛИЩА')
        return self

    async def get_by_id_all(self, instance_list: list) -> None:
        """- получить список """
        self.__storage.client.get_object(
            bucket_name=self.__storage.get_bucket(settings.MINIO_CLIENT_NAME_BUCKETS),
            object_name=await get_path(instance),
        )

    async def get_link(self, context_type=False):
        """- получить ссылку на файл """
        if not self.__object:
            return None

        return self.__storage.client.get_presigned_url(
            method='GET',
            bucket_name=self.__object.bucket_name,
            object_name=self.__object.object_name,
            response_headers={"response-content-type": "application/octet-stream"} if context_type else None,
        )


class StorageRepository(Repository):
    ...
