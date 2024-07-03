from abc import ABC, abstractmethod

from sqlalchemy import select
from typing import Type, Sequence, Any

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.v1.pictures.models import pictures


class AbstractRepository(ABC):

    @abstractmethod
    async def create(self, *args, **kwargs) -> None:
        """- создать """
        raise NotImplementedError

    @abstractmethod
    async def get_by_id_all(self, *args, **kwargs) -> None:
        """- получить список """
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, *args, **kwargs) -> None:
        """- получить по ID """
        raise NotImplementedError


class Repository(AbstractRepository):
    model = None

    def __init__(self, db: AsyncSession):
        self.__db = db

    async def create(self, data: dict) -> Type[Any]:
        """- создать """
        instance = await self.model.create(data)
        self.__db.add(instance)
        await self.__db.commit()
        await self.__db.refresh(instance)
        return instance

    async def get_by_id(self, pk: int) -> Any:
        """- получить по ID """
        instance = await self.__db.get(self.model, pk)

        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'ID {id} НЕ НАЙДЕН')
        return instance

    async def get_by_id_all(self, project_id: int, skip: int = 0, limit: int = 100) -> Sequence[Any]:
        """- получить список """
        instance = await self.__db.execute(
            select(self.model).where(self.model.project_id == project_id).offset(skip).limit(limit)
        )

        scalars_all = instance.scalars().all()

        if not scalars_all:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'PROJECT ID {project_id} НЕ НАЙДЕН')
        return scalars_all


class PictureRepository(Repository):
    model = pictures.Picture

