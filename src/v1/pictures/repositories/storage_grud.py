from abc import ABC, abstractmethod

from sqlalchemy import select
from typing import Type, Sequence, Any

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.core.storages.manager import StorageManager


class AbstractRepository(ABC):

    @abstractmethod
    async def get_all(self, *args, **kwargs) -> None:
        """- получить список """
        raise NotImplementedError

    @abstractmethod
    async def add(self, *args, **kwargs) -> None:
        """- создать """
        raise NotImplementedError


class Repository(AbstractRepository):

    def __init__(self, db: AsyncSession, storage_manager: StorageManager):
        self.__db = db
        self.__storage = storage_manager

    async def get_all(self, pk: int, skip: int = 0, limit: int = 100) -> Sequence[Any]:
        """- получить список """
        # TODO: Описать получение всех файлов из хранилища по указанному id проекта project_id
        # instance = await self.db.execute(select(self.model).offset(skip).limit(limit))
        # return instance.scalars().all()

    # async def get_one(self, pk: int) -> Type[Any]:
    #     """- получить по pk """
        # ...
        # if not instance:
        #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ID НЕ НАЙДЕН')
        # return instance

    async def add(self, path: str) -> Type[Any]:
        """- создать """
        # TODO: Описать добавление файлов в хранилище по указанному пути в виде project_id / instance_id / filename


class StorageRepository(Repository):
    ...

