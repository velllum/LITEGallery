from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """- настройки """
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    WEB_HOST: str
    WEB_PORT: int
    WEB_ALLOW_ORIGINS: str
    WEB_ALLOW_HOSTS: str
    WEB_DEBUG: bool
    WEB_RELOAD: bool
    WEB_SECRET_KEY: str

    REDIS_HOST: str
    REDIS_PORT: int

    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: int

    @property
    def DATABASE_URL_ASYNCPG(self) -> str:
        """- асинхронный драйвер """
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_PSYCOPG(self):
        """- синхронный драйвер """
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def REDIS_URL(self):
        """- ссылка redis """
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"

    model_config = SettingsConfigDict(env_file='./docker/env/dev/.env')


settings = Settings()

