from fastapi import APIRouter, Depends, HTTPException, Response, Query
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from webapp.crud.feedback.feedback import create_user_feedback
from webapp.crud.food.shop import get_shop
from webapp.crud.user.user import get_user
from webapp.db.postgres import get_session
from webapp.schema.feedback.feedback import FeedbackData
from webapp.utils.auth.jwt import jwt_auth

from webapp.crud.feedback.feedback import get_feedback_from_shop_id

from webapp.crud.feedback.feedback import get_feedback_by_id

router = APIRouter()


@router.post("/{shop_id}")
async def create_feedback(
    shop_id: int,
    data: FeedbackData,
    session: AsyncSession = Depends(get_session),
    access_token=Depends(jwt_auth.validate_token),
):
    user_id = access_token.get("user_id")
    user = await get_user(session, user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    shop = await get_shop(session, shop_id)
    feedback = await create_user_feedback(session, data, user, shop)
    return ORJSONResponse(content="success", status_code=status.HTTP_201_CREATED)

@router.get("/{shop_id}")
async def get_feedback(
    shop_id: int,
    session: AsyncSession = Depends(get_session),
    limit: int = Query(5, description="Number of shops to return"),
    offset: int = Query(0, description="Offset from the beginning of the list"),
):
    feedback = await get_feedback_from_shop_id(session, shop_id, limit, offset)
    feedbacks = [feeed.to_dict() for feeed in feedback]
    if not feedbacks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No product found"
        )
    return ORJSONResponse(content=feedbacks, status_code=status.HTTP_200_OK)


@router.get("/fb/{fb_id}")
async def get_feedback_info(
    fb_id: int,
    session: AsyncSession = Depends(get_session),
):
    feedback = await get_feedback_by_id(session, fb_id)
    return ORJSONResponse(content=feedback.to_dict(), status_code=status.HTTP_200_OK)