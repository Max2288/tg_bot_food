from sqlalchemy import select
from geoalchemy2.functions import ST_DWithin, ST_GeogFromText
from webapp.models.food.shop import Shop
from webapp.models.food.address import Address

KM_CONTAINS = 1000


async def get_near_shops(session, latitude, longitude, radius=10):
    distance_query = select(Shop)
    if latitude is not None and longitude is not None:
        point = ST_GeogFromText(f"POINT({longitude} {latitude})", srid=4326)
        distance_query = distance_query.join(Address).filter(
            ST_DWithin(Address.coordinates, point, KM_CONTAINS * radius)
        )
    result = await session.execute(distance_query)
    return result.scalars().all()