import sqlalchemy as sa
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql import func

from src.core.database import Base


class Picture(Base):
    """- модель хранения картинки """

    __tablename__ = "pictures"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    filename = Column(String, index=True, nullable=False)
    project_id = Column(Integer, index=True, nullable=False)

    # uploaded, processing, done, error (загружено, обработка, выполнено, ошибка)
    # меняется по состоянию работы websocket
    state = Column(String, index=True, nullable=False, default="uploaded")

    created_date = sa.Column(sa.DateTime, server_default=func.now())
    updated_date = sa.Column(sa.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} Picture(id={self.id!r}, country={self.country!r}, city={self.city!r})"

    @staticmethod
    async def create(data):
        """- создать новый объект """
        instance = Picture(**data)
        return instance
