import enum
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class BaseEnum(enum.Enum):

    @classmethod
    def to_dict(cls) -> dict:
        return {e.name: e.value for e in cls}

    @classmethod
    def keys(cls) -> list:
        return cls._member_names_

    @classmethod
    def values(cls) -> list:
        return list(cls._value2member_map_.keys())


class VersionNameEnum(tuple, BaseEnum):
    ORIGINAL: tuple = 'original', 0, 0
    THUMB: tuple = 'thumb', 150, 120
    BIGTHUMB: tuple = 'bigthumb', 700, 700
    BIG1920: tuple = 'big1920', 1920, 1080
    D2500: tuple = 'd2500', 2500, 2500

    @property
    def title(self) -> Any:
        """- наименование """
        return self.value[0]

    @property
    def size(self):
        """- получить данные размера """
        return self.value[1], self.value[2]

    @property
    def length(self):
        """- длина """
        return self.value[1]

    @property
    def width(self):
        """- ширина """
        return self.value[2]


class ExtEnum(str, BaseEnum):
    # TODO: лучший вариан держать список с расширениями в базе
    PNG: str = 'png'
    JPEG: str = 'jpeg'
    JPG: str = 'jpg'


class StateEnum(str, BaseEnum):
    UPLOADED: str = 'uploaded'
    PROCESSING: str = 'processing'
    DONE: str = 'done'
    ERROR: str = 'error'


class Base(BaseModel):
    id: int
    state: str
    to_fit: bool
    project_id: int
    original_filename: str
    created_date: datetime
    updated_date: datetime
    model_config = ConfigDict(from_attributes=True)


class Version(BaseModel):
    original: str
    thumb: str = None
    bigthumb: str = None
    big1920: str = None
    d2500: str = None


class Upload(Base):
    version_link_load: Version
    version_link_download: Version


class Get(Base):
    version_link_load: Version
    version_link_download: Version

