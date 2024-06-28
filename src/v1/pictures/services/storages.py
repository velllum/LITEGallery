from typing import Type, Any

from fastapi import UploadFile

from src.v1.pictures.models import Picture
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
            'version_link': Version(original=await self.__storage.get_link()),
            'version_link_download': Version(original=await self.__storage.get_link(True)),
        })
        return dct

    # async def get_one(self, pk: int):
    #     """- получить по pk """
    #     self.__instance = await self.storage.get_one(pk)

    async def get_file_all(self, list_instance: list) -> list:
        """- получить список """
        # return [await instance.feature() for instance in await self.storage.get_all(pk, skip, limit)]
        list_dct = []
        for instance in list_instance:
            await self.__storage.get_file_all(instance)
