from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    country: str
    city: str

    model_config = ConfigDict(from_attributes = True)


class Get(Base):
    id: int
    created_date: datetime
    updated_date: datetime


class Add(Base):
    ...



