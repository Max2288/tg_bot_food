from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import ORJSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.db.postgres import get_session


from webapp.crud.food.product import get_products_by_shop

from webapp.crud.food.shop import get_shop

router = APIRouter()


@router.get("/{id}")
async def get_products_with_shop(
        id: int,
        session: AsyncSession = Depends(get_session)
) -> ORJSONResponse:
    products = await get_products_by_shop(session, id)
    if products is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found")
    shop = await get_shop(session, id)
    if shop is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No shop found")
    return ORJSONResponse(
        content={
            "products": [product.to_dict() for product in products],
            "shop": shop.to_dict()
        }
    )
