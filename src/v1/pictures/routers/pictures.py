from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, Form, File


from src.v1.pictures.dependens.pictures_service import get_picture_service, get_storage_service
from src.v1.pictures.schemas.pictures import Get, Upload
from src.v1.pictures.services import PictureService, StorageService

router = APIRouter(prefix='/pictures', tags=['pictures'])

picture_service = Annotated[PictureService, Depends(get_picture_service)]
storage_service = Annotated[StorageService, Depends(get_storage_service)]


@router.post('/upload', response_model=Upload)
async def upload(picture: picture_service,
                 storage: storage_service,
                 file: UploadFile = File(...),
                 project_id: int = Form(...)):
    """- Загрузить файл на сервер  """
    instance = await picture.create(filename=file.filename, project_id=project_id)
    await storage.add(file, instance.id, project_id)
    return instance


@router.get('/{pk}', response_model=Get)
async def get_all(service: picture_service, pk: int, skip: int = 0, limit: int = 100):
    """- получить список """
    return await service.get_all(pk, skip=skip, limit=limit)

