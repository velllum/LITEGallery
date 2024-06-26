import os
from typing import Tuple

from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from src.core.database import Base


class Picture(Base):
    """- модель хранения картинки """

    __tablename__ = "pictures"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, index=True, nullable=False)
    # uploaded, processing, done, error (загружено, обработка, выполнено, ошибка)
    # меняется по состоянию работы websocket
    state = Column(String, index=True, nullable=False, default="uploaded")

    created_date = Column(DateTime, server_default=func.now())
    updated_date = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id!r}, project_id={self.project_id!r}, state={self.state!r})"

    async def get_full_path(self, new_name_file, old_name_file) -> str:
        """- полный путь к файлу """
        name, ext = os.path.splitext(old_name_file)
        return f"{await self.get_path()}/{new_name_file}{ext}"

    async def get_path(self) -> str:
        """- получить путь до файла """
        return f"{self.project_id}/{self.id}"

    @staticmethod
    async def create(data):
        """- создать новый объект """
        instance = Picture(**data)
        return instance

    @staticmethod
    async def update_field(instance, attr, value):
        """- создать новый объект """
        if hasattr(instance, attr):
            setattr(instance, attr, value)
