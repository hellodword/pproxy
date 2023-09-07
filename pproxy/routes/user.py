from typing import Union
from fastapi import APIRouter


router = APIRouter()


@router.get("/{user_id_or_username}")
async def query_user(*, user_id_or_username: Union[str, int]):
    return {"user": user_id_or_username}
