from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.sql import func

from src.core.database import Base
from src.v1.pictures.schemas.pictures import StateEnum


class Picture(Base):
    """- модель хранения картинки """

    __tablename__ = "pictures"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, index=True, nullable=False)
    # uploaded, processing, done, error (загружено, обработка, выполнено, ошибка)
    # меняется по состоянию работы websocket
    state = Column(String, index=True, nullable=False, default=StateEnum.UPLOADED.value)
    original_filename = Column(String, nullable=False)
    to_fit = Column(Boolean, index=True, default=False)
    created_date = Column(DateTime, server_default=func.now())
    updated_date = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(id={self.id!r}, project_id={self.project_id!r}, "
                f"state={self.state!r}, to_fit={self.to_fit!r}, original_filename={self.original_filename!r})")

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
