from sqlalchemy import select
from webapp.models.food.shop import Shop


async def get_shop(session, shop_id: int):
    return (await session.scalars(select(Shop).where(Shop.id == shop_id))).one_or_none()
