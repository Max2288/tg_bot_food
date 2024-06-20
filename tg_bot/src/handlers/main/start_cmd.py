from aiogram import types
from aiogram.filters.command import CommandStart

from src.buttons.main.default import get_main_keyboard
from src.handlers.main.router import main_router


@main_router.message(
    CommandStart()
)
async def cmd_start(message: types.Message) -> None:
    await message.answer('Спасибо что пришли', reply_markup=get_main_keyboard())
    return