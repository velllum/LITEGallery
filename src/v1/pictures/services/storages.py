from typing import Type

from fastapi import UploadFile

from src.v1.pictures.repositories.storage_grud import StorageRepository
from src.v1.pictures.schemas.pictures import Upload


class StorageService:
    """- сервис (GRUD операций) хранилища """

    def __init__(self, storage: StorageRepository):
        self.storage = storage

    async def add(self, file: UploadFile, instance: Type):
        """- создать """
        return await self.storage.add(file, instance)

    # async def get_one(self, pk: int):
    #     """- получить по pk """
    #     self.__instance = await self.storage.get_one(pk)

    async def get_by_id_all(self, pk: int, skip: int = 0, limit: int = 100):
        """- получить список """
        # return [await instance.feature() for instance in await self.storage.get_all(pk, skip, limit)]

