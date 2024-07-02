import io
import os
from abc import ABC, abstractmethod

from typing import Type, Any

from fastapi import HTTPException, UploadFile
from minio.helpers import ObjectWriteResult
from starlette import status

from src.core.configs import settings
from src.core.storages.manager import StorageManager
from src.v1.pictures.models.pictures import Picture
from src.v1.pictures.schemas.pictures import VersionNameEnum
from src.v1.pictures.utils.pictures import get_full_path, get_path


class AbstractRepository(ABC):

    @abstractmethod
    async def add(self, *args, **kwargs) -> None:
        """- создать """
        raise NotImplementedError

    @abstractmethod
    async def get_file_all(self, *args, **kwargs) -> None:
        """- получить список """
        raise NotImplementedError


class Repository(AbstractRepository):

    def __init__(self, storage_manager: StorageManager):
        self.__storage = storage_manager
        self.__object = None
        self.__list_objects = None
        self.__instance = None

    async def add(self, file: UploadFile, instance: Type | Picture) -> ObjectWriteResult:
        """- добавить """
        self.__object = self.__storage.client.put_object(
            bucket_name=self.__storage.get_bucket(settings.MINIO_CLIENT_NAME_BUCKETS),
            object_name=await get_full_path(instance, VersionNameEnum.ORIGINAL.value, file.filename),
            data=io.BytesIO(file.file.read()),
            content_type=file.content_type,
            length=file.size
        )
        if not self.__object:
            raise HTTPException(status_code=status.HTTP_200_OK, detail='ОШИБКА ДОБАВЛЕНИЯ В ХРАНИЛИЩА')
        return self.__object

    async def get_file_all(self, instance: Type | Picture) -> list[Any]:
        """- получить список """
        list_objects = self.__storage.client.list_objects(
            bucket_name=self.__storage.get_bucket(settings.MINIO_CLIENT_NAME_BUCKETS),
            prefix=await get_path(instance),
        )
        self.__list_objects = list(list_objects)
        return self.__list_objects

    async def get_link(self, context_type: bool = False) -> str | None:
        """- получить ссылку на файл """
        if not self.__object:
            return None

        return await self.__generate_link(self.__object, context_type)

    async def get_link_all(self, instance: Type | Picture, context_type: bool = False) -> dict[Any, str] | None:
        """- получить ссылку на файл """
        if not self.__list_objects:
            return None

        dct = {}

        for _object in self.__list_objects:
            name, ext = os.path.splitext(_object.object_name.removeprefix(await get_path(instance)))
            dct[name] = await self.__generate_link(_object, context_type)

        return dct

    async def __generate_link(self, _object:  ObjectWriteResult, context_type: bool) -> str:
        """- сформировать ссылку """
        return self.__storage.client.get_presigned_url(
            method='GET',
            bucket_name=_object.bucket_name,
            object_name=_object.object_name,
            response_headers={"response-content-type": "application/octet-stream"} if context_type else None,
        )


class StorageRepository(Repository):
    ...
