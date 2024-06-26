from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    id: int
    state: str
    filename: str
    project_id: int
    # path: str
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)


class Version(BaseModel):
    original: str
    thumb: str
    big_thumb: str
    big_1920: str
    d2500: str


class Upload(Base):
    # original_link: str
    ...


class Get(Base):
    version_link: Version
    version_link_download: Version

