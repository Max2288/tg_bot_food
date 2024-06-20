from aiogram import types
from aiogram.filters.callback_data import CallbackData


class ShopCallback(CallbackData, prefix="shop"):
    id: int
