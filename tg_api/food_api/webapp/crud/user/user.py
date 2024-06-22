from sqlalchemy import select, exists
from sqlalchemy.ext.asyncio import AsyncSession

from webapp.models.user.user import User

from webapp.schema.user.user import UserRegister


async def check_user(session: AsyncSession, user_id: int) -> bool:
    query = select(exists().where(User.id == user_id))
    return bool(await session.scalar(query))



async def create_user(session: AsyncSession, user_info: UserRegister):
    try:
        user = User(
            id=user_info.id,
            username=user_info.username,
        )
        session.add(user)
        await session.commit()
        return user
    except Exception as err:
        await session.rollback()
        return None

async def get_user(session: AsyncSession, user_id: int) -> User:
    return (
        await session.scalars(
            select(User).where(
                User.id == user_id
            )
        )
    ).one_or_none()