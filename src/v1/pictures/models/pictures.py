import sqlalchemy as sa
from sqlalchemy.sql import func

from src.core.database import Base


class Picture(Base):
    """- модель хранения картинки """

    __tablename__ = "pictures"
    # __table_args__ = (sa.UniqueConstraint('country', 'city', name='uq_capital_cities_country_city'),)

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    country = sa.Column(sa.String, index=True, nullable=False)
    city = sa.Column(sa.String, index=True, nullable=False)

    created_date = sa.Column(sa.DateTime, server_default=func.now())
    updated_date = sa.Column(sa.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self) -> str:
        return f"Picture(id={self.id!r}, country={self.country!r}, city={self.city!r})"

    @staticmethod
    async def create(data):
        """- создать новый объект """
        instance = Picture()
        return instance

    @staticmethod
    async def update(instance, data):
        """- создать новый объект """

        return instance

