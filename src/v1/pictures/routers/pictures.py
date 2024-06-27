from typing import Annotated, List

from fastapi import APIRouter, Depends, UploadFile, Form, File


from src.v1.pictures.dependens.pictures_service import get_picture_service, get_storage_service
from src.v1.pictures.schemas.pictures import Get, Upload
from src.v1.pictures.services import PictureService, StorageService

router = APIRouter(prefix='/gallery', tags=['gallery'])

picture_service = Annotated[PictureService, Depends(get_picture_service)]
storage_service = Annotated[StorageService, Depends(get_storage_service)]


@router.post('/upload', response_model=Upload)
async def upload(picture: picture_service, storage: storage_service, file: UploadFile = File(...),
                 project_id: int = Form(...)):
    """- Загрузить файл на сервер  """
    # TODO: сделать проверку на допустимые файловые расширения
    picture_instance = await picture.create(project_id=project_id)
    storage_dict = await storage.add(file, picture_instance)
    return storage_dict


@router.get('/{project_id}/pictures', response_model=List[Get])
async def get_by_id_all(service: picture_service, storage: storage_service, project_id: int, skip: int = 0, limit: int = 100):
    """- получить список """
    instance_list = await service.get_by_id_all(project_id, skip=skip, limit=limit)
    storage_list = await storage.get_by_id_all(instance_list)
    return storage_list

