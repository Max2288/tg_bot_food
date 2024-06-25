from typing import Annotated
from uuid import UUID

from conf.config import settings
from fastapi import Header


async def validate_and_check_api_key(authorization: Annotated[str, Header()]) -> bool:
    _, token = authorization.split()
    UUID(token)
    return settings.API_KEY == token
