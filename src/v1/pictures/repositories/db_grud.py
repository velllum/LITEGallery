from abc import ABC, abstractmethod

from sqlalchemy import select
from typing import Type, Sequence, Any

from asyncpg import UniqueViolationError
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
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
        self.db = db

    async def get_all(self, skip: int = 0, limit: int = 100) -> Sequence[Any]:
        """- получить список """
        instance = await self.db.execute(select(self.model).offset(skip).limit(limit))
        return instance.scalars().all()

    async def get_one(self, pk: int) -> Type[Any]:
        """- получить по pk """
        instance = await self.db.get(self.model, pk)
        if not instance:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID НЕ НАЙДЕН')
        return instance

    async def create(self, data: dict) -> Type[Any]:
        """- создать """
        try:
            instance = await self.model.create(data)
            self.db.add(instance)
            await self.db.commit()
            await self.db.refresh(instance)
            return instance
        except IntegrityError or UniqueViolationError:
            raise HTTPException(status_code=status.HTTP_200_OK, detail='СТРАНА И ГОРОД УЖЕ СУЩЕСТВУЮТ')


class PictureRepository(Repository):
    model = Picture
