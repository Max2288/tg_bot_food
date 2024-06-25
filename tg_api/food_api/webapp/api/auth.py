from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, Response
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from webapp.crud.user.user import check_user, create_user, get_user
from webapp.db.postgres import get_session
from webapp.schema.user.user import UserLogin, UserRegister
from webapp.utils.auth.api_key import validate_and_check_api_key
from webapp.utils.auth.jwt import jwt_auth

router = APIRouter()


@router.post("/register")
async def register(
    body: UserRegister,
    auth: Annotated[str, Header()],
    session: AsyncSession = Depends(get_session),
):
    valid_token = await validate_and_check_api_key(auth)
    if not valid_token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    user_exists = await check_user(session, body.id)
    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    new_user = await create_user(session, body)
    if new_user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return Response(content="success", status_code=status.HTTP_201_CREATED)


@router.post("/login")
async def auth_login_handler(
    body: UserLogin,
    auth: Annotated[str, Header()],
    session: AsyncSession = Depends(get_session),
) -> ORJSONResponse:
    try:
        valid_token = await validate_and_check_api_key(auth)
        if not valid_token:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

        user = await get_user(session, body.id)

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return ORJSONResponse({"access_token": jwt_auth.create_token(user)})
    except HTTPException as http_err:
        raise http_err
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
