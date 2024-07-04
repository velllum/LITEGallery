import os
from typing import Type

from src.v1.pictures.models.pictures import Picture


async def get_full_path_original_file(instance: Type, new_name_file: str) -> str:
    """- полный путь к файлу """
    return f"{await get_path(instance)}{await get_original_filename(new_name_file, instance.original_filename)}"


async def get_original_filename(new_name_file: str, old_name_file: str) -> str:
    """- получить наименование оригинального файла """
    _, ext = os.path.splitext(old_name_file)
    return f'{new_name_file}{ext}'


async def get_path(instance: Type | Picture) -> str:
    """- получить путь до файла """
    return f"{instance.project_id}/{instance.id}/"

