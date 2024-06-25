from fastapi import APIRouter
from src.api.tg import tg

tg_router = APIRouter(prefix="")

tg_router.include_router(tg.router)
