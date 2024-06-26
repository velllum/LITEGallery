import os
from typing import Type

from src.v1.pictures.models import Picture


async def get_full_path(instance: Type, new_name_file: str, old_name_file: str) -> str:
    """- полный путь к файлу """
    name, ext = os.path.splitext(old_name_file)
    return f"{await get_path(instance)}/{new_name_file}{ext}"


async def get_path(instance: Type | Picture) -> str:
    """- получить путь до файла """
    return f"{instance.project_id}/{instance.id}"

