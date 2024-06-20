from aiogram import types

from src.callback.main.back import BackCallback


def get_back_button(previous_id: int) -> types.InlineKeyboardMarkup:
    kb = [
        [
            types.InlineKeyboardButton(
                text='Назад',
                callback_data=BackCallback(previous_id=previous_id).pack()
            ),
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)
