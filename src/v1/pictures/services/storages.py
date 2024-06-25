from fastapi import UploadFile

from src.v1.pictures.repositories.storage_grud import StorageRepository


class StorageService:
    """- сервис (GRUD операций) хранилища """

    def __init__(self, storage: StorageRepository):
        self.storage = storage

    async def add(self, file: UploadFile, instance_id: int, project_id: int):
        """- создать """
        # TODO: запустить фоновую задачу для сборки и добавления сгенерированных файлов в хранилище
        # TODO: возможно проработка работы запуск фоновых задач в хуках при добавлении новых данных в в базу

        return await self.storage.add(file, instance_id, project_id)

    # async def get_one(self, pk: int):
    #     """- получить по pk """
    #     self.__instance = await self.storage.get_one(pk)

    async def get_all(self, pk: int, skip: int = 0, limit: int = 100):
        """- получить список """
        return [await instance.feature() for instance in await self.storage.get_all(pk, skip, limit)]

