from typing import Any, Sequence

from src.v1.pictures.repositories.db_grud import PictureRepository


class PictureService:
    """- сервис (GRUD операций) БД """

    def __init__(self, grud: PictureRepository):
        self.__grud = grud

    async def create(self, **data) -> type:
        """- создать """
        return await self.__grud.create(data)

    async def get_by_id_all(self, project_id: int, skip: int = 0, limit: int = 100) -> Sequence[Any]:
        """- получить список """
        return await self.__grud.get_by_id_all(project_id, skip, limit)



