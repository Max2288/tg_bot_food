from typing import Optional

from conf.config import settings
from src.utils.request import do_request
from starlette.status import HTTP_200_OK, HTTP_201_CREATED


async def create_user_request(user_id: int, username: str) -> bool:

    _, status = await do_request(
        f"api/v1/auth/register",
        headers={"auth": f"Bearer {settings.API_KEY}"},
        params={"id": user_id, "username": username},
    )
    if status != HTTP_201_CREATED:
        return False

    return True


async def get_user_token_request(user_id: int) -> Optional[str]:
    response, status = await do_request(
        "api/v1/auth/login",
        headers={"auth": f"Bearer {settings.API_KEY}"},
        params={"id": user_id},
    )
    if status != HTTP_200_OK:
        return None

    return response["access_token"]
