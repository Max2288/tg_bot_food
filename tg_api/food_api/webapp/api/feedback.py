from fastapi import APIRouter, Depends, Response, HTTPException
from fastapi.responses import ORJSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.db.postgres import get_session

from webapp.utils.auth.jwt import jwt_auth

from webapp.schema.feedback.feedback import FeedbackData

from webapp.crud.feedback.feedback import create_user_feedback

from webapp.crud.user.user import get_user

from webapp.crud.food.shop import get_shop

router = APIRouter()


@router.post("/{shop_id}")
async def create_feedback(
    shop_id : int,
    data: FeedbackData,
    session: AsyncSession = Depends(get_session),
    access_token = Depends(jwt_auth.validate_token)
):
    user_id =access_token.get('user_id')
    user = await get_user(session, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    shop = await get_shop(session, shop_id)
    feedback = await create_user_feedback(session, data, user, shop)
    return ORJSONResponse(content='success', status_code=status.HTTP_201_CREATED)
