from fastapi import APIRouter

from webapp.api import test, search, shop, product

router = APIRouter()

router.include_router(test.router, prefix="/test2", tags=["test"])
router.include_router(search.router, prefix="/search", tags=["Search"])
router.include_router(shop.router, prefix="/shop", tags=["Shop"])
router.include_router(product.router, prefix="/product", tags=["Product"])