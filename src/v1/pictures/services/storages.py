from src.v1.pictures.repositories.db_grud import PictureRepository
from src.v1.pictures.repositories.storage_grud import StorageRepository


class StorageService:
    """- сервис (GRUD операций) хранилища """

    def __init__(self, storage: StorageRepository):
        self.storage = storage

    async def get_all(self, pk: int, skip: int = 0, limit: int = 100):
        """- получить список """
        return [await instance.feature() for instance in await self.storage.get_all(pk, skip, limit)]

    # async def get_one(self, pk: int):
    #     """- получить по pk """
    #     self.__instance = await self.storage.get_one(pk)

    async def add(self, file, instance_id, project_id):
        """- создать """
        # TODO: запустить фоновую задачу для сборки и добавления сгенерированных файлов в хранилище
        path = f"{project_id}/{instance_id}/{file.filename}"
        return await self.storage.add(path)

