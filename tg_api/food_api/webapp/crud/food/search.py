from geoalchemy2.functions import ST_DWithin, ST_GeogFromText
from sqlalchemy import select
from webapp.models.food.address import Address
from webapp.models.food.shop import Shop

KM_CONTAINS = 1000


async def get_near_shops(session, longitude, latitude, limit, offset, radius=10):
    distance_query = select(Shop)
    if latitude is not None and longitude is not None:
        point = ST_GeogFromText(f"POINT({latitude} {longitude})", srid=4326)
        distance_query = distance_query.join(Address).filter(
            ST_DWithin(Address.coordinates, point, KM_CONTAINS * radius)
        )
    result = await session.execute(distance_query.limit(limit).offset(offset))
    return result.scalars().all()
