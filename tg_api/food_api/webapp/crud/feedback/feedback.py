from sqlalchemy.ext.asyncio import AsyncSession
from webapp.models.feedback.feedback import Feedback
from webapp.models.food.shop import Shop
from webapp.models.user.user import User
from webapp.schema.feedback.feedback import FeedbackData
from sqlalchemy import exists, select


async def create_user_feedback(
        session: AsyncSession, feedback_info: FeedbackData, user: User, shop: Shop
):
    feedback = Feedback(
        score=feedback_info.score,
        description=feedback_info.description,
        user=user.id,
        shop=shop.id,
    )
    session.add(feedback)
    await session.commit()
    return feedback


async def get_feedback_from_shop_id(session: AsyncSession, shop_id: int, limit, offset):
    return await session.scalars(select(Feedback).where(Feedback.shop == shop_id).limit(limit)
                                 .offset(offset))


async def get_feedback_by_id(session: AsyncSession, fb_id: int,):
    return (await session.scalars(select(Feedback).where(Feedback.id == fb_id))).one_or_none()