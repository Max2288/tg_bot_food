from fastapi import APIRouter
from webapp.api import auth, feedback, minio, product, search, shop, test

router = APIRouter()

router.include_router(test.router, prefix="/test2", tags=["test"])
router.include_router(search.router, prefix="/search", tags=["Search"])
router.include_router(shop.router, prefix="/shop", tags=["Shop"])
router.include_router(product.router, prefix="/product", tags=["Product"])
router.include_router(minio.router, prefix="/minio", tags=["Minio"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(feedback.router, prefix="/feedback", tags=["Feedback"])
