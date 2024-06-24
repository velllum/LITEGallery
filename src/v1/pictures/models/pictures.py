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
    state = Column(String, index=True, nullable=False, default="uploaded")  # uploaded, processing, done, error
    original = Column(String, nullable=False)

    thumb = Column(String, nullable=True)
    bigthumb = Column(String, nullable=True)
    big1920 = Column(String, nullable=True)
    d2500 = Column(String, nullable=True)

    created_date = sa.Column(sa.DateTime, server_default=func.now())
    updated_date = sa.Column(sa.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} Picture(id={self.id!r}, country={self.country!r}, city={self.city!r})"

    @staticmethod
    async def create(data):
        """- создать новый объект """
        instance = Picture()
        return instance
