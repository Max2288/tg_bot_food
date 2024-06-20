import os

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from webapp.db.postgres import get_session
from sqlalchemy import select

from webapp.models.food.shop import Address
from webapp.models.food.product import Product

router = APIRouter()

@router.get("/test")
async def test(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product))
    addresses = result.scalars().all()
    return [address.to_dict() for address in addresses]
