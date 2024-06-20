

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import ORJSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from webapp.db.postgres import get_session


from webapp.crud.food.product import get_product_by_id


router = APIRouter()


@router.get("/{id}")
async def get_product(
        id: int,
        session: AsyncSession = Depends(get_session)
) -> ORJSONResponse:
    product = await get_product_by_id(session, id)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No product found")
    return ORJSONResponse(
        content=product.to_dict(),
        status_code=status.HTTP_200_OK
    )
