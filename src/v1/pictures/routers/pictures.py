from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile
from starlette import status
from starlette.responses import Response

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


@router.post('/{pk}/create', response_model=GetFeatureCollection)
async def create(service: capital_city_service, data: FeatureCollection, file: UploadFile, pk: int):
    """- создать """
    return await service.create(data)


@router.put('/{pk}', response_model=GetFeatureCollection)
async def update(service: capital_city_service, pk: int, data: FeatureCollection):
    """- обновить """
    return await service.update(pk, data)


@router.delete('/{pk}', status_code=status.HTTP_200_OK)
async def delete(service: capital_city_service, pk: int) -> Response:
    """- удалить """
    await service.delete(pk)
    return Response(status_code=status.HTTP_200_OK, content='{"detail": "ДАННЫЕ УДАЛЕНЫ"}')

