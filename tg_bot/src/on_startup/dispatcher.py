from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message

from src.handlers.main.router import main_router
from src.handlers.search.router import search_router
from aiogram.fsm.storage.memory import MemoryStorage

def setup_dispatcher(bot: Bot) -> Dispatcher:
    storage = MemoryStorage()
    dp = Dispatcher(bot=bot, storage=storage)
    dp.include_router(main_router)
    dp.include_router(search_router)

    return dp
