from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from webapp.db.postgres import get_session


from webapp.schema.food.search import ShopResponse

from webapp.crud.food.search import get_near_shops

router = APIRouter()


@router.get("/shop", response_model=list[ShopResponse])
async def get_shops(
        longitude: float = Query(None, description="Longitude of the location"),
        latitude: float = Query(None, description="Latitude of the location"),
        session: AsyncSession = Depends(get_session)
) -> ORJSONResponse:
    shops = await get_near_shops(session, longitude, latitude)
    if not shops:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No shops found")
    return ORJSONResponse(content=[shop.to_dict() for shop in shops], status_code=status.HTTP_200_OK)

