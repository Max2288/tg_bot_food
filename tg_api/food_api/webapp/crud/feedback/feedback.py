from sqlalchemy.ext.asyncio import AsyncSession

from webapp.schema.feedback.feedback import FeedbackData

from webapp.models.feedback.feedback import Feedback

from webapp.models.user.user import User

from webapp.models.food.shop import Shop


async def create_user_feedback(session: AsyncSession, feedback_info: FeedbackData, user: User, shop: Shop):
    feedback = Feedback(
        score=feedback_info.score,
        description=feedback_info.description,
        user=user.id,
        shop=shop.id
    )
    session.add(feedback)
    await session.commit()
    return feedback
