from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    id: int
    state: str
    project_id: int
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)


class Version(BaseModel):
    original: str
    thumb: str = None
    big_thumb: str = None
    big_1920: str = None
    d2500: str = None


class Upload(Base):
    version_link: Version
    version_link_download: Version


class Get(Base):
    version_link: Version
    version_link_download: Version

