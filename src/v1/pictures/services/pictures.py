from typing import Any

from src.v1.pictures.repositories.grud import PictureRepository
from src.v1.pictures.schemas.pictures import FeatureCollection

feature_collection = dict[str, str | list[Any]]


class PictureService:
    """- сервисы (GRUD операции) столицы городов """

    def __init__(self, grud: PictureRepository):
        self.__features = []
        self.__instance = Any
        self.grud = grud

    async def get_all(self, skip: int = 0, limit: int = 100) -> feature_collection:
        """- получить список пользователей """
        self.__features = [await instance.feature() for instance in await self.grud.get_all(skip, limit)]
        return await self.__list_feature_collection()

    async def get_one(self, pk: int) -> feature_collection:
        """- получить по pk """
        self.__instance = await self.grud.get_one(pk)
        return await self.__feature_collection()

    async def create(self, data: FeatureCollection) -> feature_collection:
        """- создать """
        self.__instance = await self.grud.create(data)
        return await self.__feature_collection()

    async def __feature_collection(self) -> feature_collection:
        """- получить коллекцию в стиле GEOJSON """
        self.__features.append(await self.__instance.feature())
        return await self.__list_feature_collection()

    async def __list_feature_collection(self) -> feature_collection:
        """- получить коллекцию в стиле GEOJSON """
        return {"type": "FeatureCollection", "features": self.__features}


