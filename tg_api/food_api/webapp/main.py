from contextlib import asynccontextmanager
from typing import AsyncIterator

from conf.config import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from webapp.api import api


def setup_middleware(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def setup_routers(app: FastAPI) -> None:
    PATH_PREFIX = settings.PATH_PREFIX
    app.include_router(api.router, prefix=PATH_PREFIX)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    print("START APP")
    yield
    print("END APP")


def create_app() -> FastAPI:
    app = FastAPI(docs_url="/swagger", lifespan=lifespan)

    setup_middleware(app)
    setup_routers(app)

    return app
