from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    filename: str
    project_id: int


class Upload(Base):
    ...


class Version(BaseModel):
    original: str
    thumb: str
    big_thumb: str
    big_1920: str
    d2500: str


class Get(Base):
    id: int
    state: str  # uploaded, processing, done, error
    version: Version
    created_date: datetime
    updated_date: datetime

    model_config = ConfigDict(from_attributes=True)

