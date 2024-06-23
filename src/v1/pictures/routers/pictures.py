from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, Form, File


from src.v1.pictures.dependens.pictures_service import get_capital_city_service
from src.v1.pictures.schemas.pictures import FeatureCollection, GetFeatureCollection
from src.v1.pictures.services import PictureService

router = APIRouter(prefix='/pictures', tags=['pictures'])
capital_city_service = Annotated[PictureService, Depends(get_capital_city_service)]


@router.get('/', response_model=GetFeatureCollection)
async def get_all(service: capital_city_service, skip: int = 0, limit: int = 100):
    """- получить список """
    return await service.get_all(skip=skip, limit=limit)


@router.get('/{pk}', response_model=GetFeatureCollection)
async def get_by_pk(service: capital_city_service, pk: int):
    """- получить по pk """
    return await service.get_one(pk)


@router.post('/create', response_model=GetFeatureCollection)
async def create(service: capital_city_service, file: UploadFile = File(...), project_id: int = Form(...)):
    """- создать """
    return await service.create(data)


