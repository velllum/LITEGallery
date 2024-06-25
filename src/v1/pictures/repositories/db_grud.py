from abc import ABC, abstractmethod

from sqlalchemy import select
from typing import Type, Sequence, Any

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.v1.pictures.models import Picture


class AbstractRepository(ABC):

    @abstractmethod
    async def get_all(self, *args, **kwargs) -> None:
        """- получить список """
        raise NotImplementedError

    @abstractmethod
    async def get_one(self, *args, **kwargs) -> None:
        """- получить экземпляр """
        raise NotImplementedError

    @abstractmethod
    async def create(self, *args, **kwargs) -> None:
        """- создать """
        raise NotImplementedError


class Repository(AbstractRepository):
    model = None

    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_all(self, skip: int = 0, limit: int = 100) -> Sequence[Any]:
        """- получить список """
        instance = await self.__db.execute(select(self.model).offset(skip).limit(limit))
        return instance.scalars().all()

    async def get_one(self, pk: int) -> Type[Any]:
        """- получить по pk """
        instance = await self.__db.get(self.model, pk)
        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID НЕ НАЙДЕН')
        return instance

    async def create(self, data: dict) -> Type[Any]:
        """- создать """
        instance = await self.model.create(data)
        self.__db.add(instance)
        await self.__db.commit()
        await self.__db.refresh(instance)
        return instance


class PictureRepository(Repository):
    model = Picture