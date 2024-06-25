from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from src.handlers.feedback.router import feedback_router
from src.handlers.main.router import main_router
from src.handlers.search.router import search_router
from src.integrations.redis import redis
from src.middleware.auth import AuthMiddleware


def setup_dispatcher(bot: Bot) -> Dispatcher:
    storage = RedisStorage(redis)
    dp = Dispatcher(bot=bot, storage=storage)
    dp.include_router(main_router)
    dp.include_router(search_router)
    dp.include_router(feedback_router)

    dp.message.middleware(AuthMiddleware())
    dp.callback_query.middleware(AuthMiddleware())

    return dp
