from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Base(BaseModel):
    country: str
    city: str

    model_config = ConfigDict(from_attributes = True)


class Delete(Base):
    ...


# =============================


class GetFeatureProperties(Base):
    id: int
    created_date: datetime
    updated_date: datetime


class GetFeature(Base):
    geometry: GetFeatureProperties
    properties: GetFeatureProperties


class GetFeatureCollection(Base):
    features: list[GetFeature]


# ==============================


class FeatureProperties(Base):
    ...


class Feature(Base):
    geometry: FeatureProperties
    properties: FeatureProperties


class FeatureCollection(Base):
    features: list[Feature]


