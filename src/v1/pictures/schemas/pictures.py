import enum
from datetime import datetime

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


class VersionNameEnum(str, BaseEnum):
    ORIGINAL: str = 'original'
    THUMB: str = 'thumb'
    BIGTHUMB: str = 'bigthumb'
    BIG1920: str = 'big1920'
    D2500: str = 'd2500'


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

