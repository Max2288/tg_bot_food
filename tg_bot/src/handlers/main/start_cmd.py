from aiogram import types
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from src.buttons.main.default import get_main_keyboard
from src.handlers.main.router import main_router
from src.requests.user import create_user_request


@main_router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext) -> None:
    access_token = (await state.get_data()).get("access_token")
    if access_token is not None:
        await message.answer("Спасибо что пришли", reply_markup=get_main_keyboard())
        return
    await create_user_request(
        user_id=message.from_user.id, username=message.from_user.username
    )
    await message.answer("Приветствуем впервые", reply_markup=get_main_keyboard())
    return
