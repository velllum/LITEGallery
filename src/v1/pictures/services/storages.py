from typing import Type, Dict, Any

from fastapi import UploadFile

from src.v1.pictures.models import Picture
from src.v1.pictures.repositories.storage_grud import StorageRepository
from src.v1.pictures.schemas.pictures import Upload


class StorageService:
    """- сервис (GRUD операций) хранилища """

    def __init__(self, storage: StorageRepository):
        self.__storage = storage

    async def add(self, file: UploadFile, instance: Type | Picture) -> dict[str | Any, Any]:
        """- создать """
        await self.__storage.add(file, instance)
        dct = dict(instance.__dict__)
        dct.update(**{'original_link': await self.__storage.get_link(),
                      'original_link_download': await self.__storage.get_link(True)})
        return dct

    # async def get_one(self, pk: int):
    #     """- получить по pk """
    #     self.__instance = await self.storage.get_one(pk)

    async def get_by_id_all(self, pk: int, skip: int = 0, limit: int = 100):
        """- получить список """
        # return [await instance.feature() for instance in await self.storage.get_all(pk, skip, limit)]
