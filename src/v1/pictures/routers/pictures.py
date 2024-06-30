from typing import Annotated, List

from fastapi import APIRouter, Depends, UploadFile, Form, File, HTTPException
from starlette import status

from src.v1.pictures.dependens.pictures_service import get_picture_service, get_storage_service
from src.v1.pictures.schemas.pictures import Get, Upload, ExtEnum
from src.v1.pictures.services import PictureService, StorageService

router = APIRouter(prefix='/gallery', tags=['gallery'])

picture_service = Annotated[PictureService, Depends(get_picture_service)]
storage_service = Annotated[StorageService, Depends(get_storage_service)]


@router.post('/upload', response_model=Upload)
async def upload(picture: picture_service, storage: storage_service,
                 to_fit: bool = Form(default=False, description='Ресайзится по длинной стороне'),
                 file: UploadFile = File(...), project_id: int = Form(...)):
    """- Загрузить файл на сервер  """

    # сделать проверку на допустимые файловые расширения
    ext = file.filename.split('.')[-1]
    ext.lower() if ext.isupper() else ext

    if ext not in ExtEnum.values():
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'ОШИБКА .{ext} ФАЙЛ С ДАННЫМ РАСШИРЕНИЕМ ЗАПРЕЩЕН ДЛЯ ЗАГРУЗКИ')

    picture_instance = await picture.create(project_id=project_id, to_fit=to_fit)
    storage_dict = await storage.add(file, picture_instance)
    return storage_dict


@router.get('/{project_id}/pictures', response_model=List[Get])
async def get_by_id_all(service: picture_service, storage: storage_service, project_id: int, skip: int = 0, limit: int = 100):
    """- получить список """
    list_instance = await service.get_by_id_all(project_id, skip=skip, limit=limit)
    list_storage = await storage.get_file_all(list_instance)
    return list_storage

