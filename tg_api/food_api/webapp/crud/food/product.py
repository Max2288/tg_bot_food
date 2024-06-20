from sqlalchemy import select

from webapp.models.food.product import Product
from webapp.models.food.shop import Shop


async def get_products_by_shop(session, shop_id: int):
    result = await session.execute(
        select(Product)
        .where(Product.shop == shop_id)
        .join(Shop)
        .order_by(Product.is_hot)
    )
    return result.scalars().all()


async def get_product_by_id(session, product_id: int):
    return (
        await session.scalars(
            select(Product).where(Product.id == product_id)
        )
    ).one_or_none()