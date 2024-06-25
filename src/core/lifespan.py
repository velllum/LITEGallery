import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.configs import settings
from src.core.database import db_manager
from src.core.routers import register_routers
from src.core.storages.manager import storage_manager
from src.v1.admins import create_admin
from tests.v1.test_pictures.conftest import add_test_data_table

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """- События продолжительности жизни """
    await start_minio()
    await start_database()
    await start_test_data()
    await start_routers(app)
    await start_admin(app)

    yield

    await close_database()


async def start_minio():
    """- регистрируем подключение к хранилищу данных """
    storage_manager.init(
        endpoint=settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ROOT_USER,
        secret_key=settings.MINIO_ROOT_PASSWORD,
        secure=False
    )
    storage_manager.make_buckets(settings.MINIO_CLIENT_NAME_BUCKETS)
    logger.info("ЗАПУСК ХРАНИЛИЩА ВЫПОЛНЕН")


async def start_database():
    """- регистрируем подключение к базе данных"""
    db_manager.init(settings.DATABASE_URL_ASYNCPG)
    logger.info("ЗАПУСК БАЗЫ ДАННЫХ ВЫПОЛНЕН")


async def start_routers(app: FastAPI):
    """- старт инициализации роутеров """
    await register_routers(app)
    logger.info("РЕГИСТРАЦИЯ РОУТОВ")


async def start_admin(app: FastAPI):
    """- регистрируем админ-панель """
    await create_admin(app)
    logger.info("ЗАПУСК АДМИН ПАНЕЛИ")


async def start_test_data():
    """- регистрируем тестовые данные """
    try:
        await add_test_data_table()
        logger.info("ДОБАВЛЕНИЕ ТЕСТОВЫХ ДАННЫХ ВЫПОЛНЕНО")
    except:
        logger.info("[ОШИБКА] ПРИ ДОБАВЛЕНИИ ТЕСТОВЫХ ДАННЫХ ВЫПОЛНЕНО")


async def close_database():
    """- закрываем базу данных"""
    await db_manager.close()
    logger.info("БАЗА ДАННЫХ ЗАКРЫТА")

