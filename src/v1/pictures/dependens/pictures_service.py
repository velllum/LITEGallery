from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_async_db
from src.v1.pictures.repositories.grud import PictureRepository
from src.v1.pictures.services import PictureService

async_db = Depends(get_async_db)


async def get_capital_city_service(db: AsyncSession = async_db) -> PictureService:
    return PictureService(PictureRepository(db))


# TODO: добавить зависимость между сервисом TaskService и PictureService

