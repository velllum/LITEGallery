from typing import Type, Any, Sequence

from fastapi import UploadFile

from src.v1.pictures.models.pictures import Picture
from src.v1.pictures.repositories.storage_grud import StorageRepository
from src.v1.pictures.schemas.pictures import Version


class StorageService:
    """- сервис (GRUD операций) хранилища """

    def __init__(self, storage: StorageRepository):
        self.__storage = storage

    async def add(self, file: UploadFile, instance: Type | Picture) -> dict[str | Any, Any]:
        """- создать """
        await self.__storage.add(file, instance)

        dct = dict(instance.__dict__)

        dct.update(**{
            'version_link_load': Version(original=await self.__storage.get_link()),
            'version_link_download': Version(original=await self.__storage.get_link(True)),
        })
        return dct

    async def get_file_all(self, list_instance: Sequence[Any]):
        """- получить список """
        lst = []
        for instance in list_instance:
            await self.__storage.get_file_all(instance)

            dct = dict(instance.__dict__)

            version_link = await self.__storage.get_link_all(instance)
            version_link_download = await self.__storage.get_link_all(instance, True)

            if not version_link or not version_link_download:
                continue

            dct.update(**{
                'version_link_load': Version(**version_link),
                'version_link_download': Version(**version_link_download),
            })
            lst.append(dct)

        return lst