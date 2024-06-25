from typing import Callable, ParamSpec

from aiogram import types

P = ParamSpec("P")

SETTINGS_FOR_NOTIFICATIONS = "Настройка уведомлений"
REVIEWS_AND_MARKS = "Отзывы и оценки"
FIND_BTN = "Найти"
NEWS_AND_ACTIONS = "Новости и акции"
SUPPORT_BTN = "Служба поддержки"


def get_main_keyboard() -> types.ReplyKeyboardMarkup:
    return _get_keyboard_user()


def _get_keyboard_user() -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=FIND_BTN)],
        [types.KeyboardButton(text=SUPPORT_BTN)],
    ]

    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def create_star_buttons():
    kb = []
    for i in range(1, 6):
        kb.append(
            [
                (
                    types.InlineKeyboardButton(
                        text="★" * i + "☆" * (5 - i), callback_data=f"rating_{i}"
                    )
                )
            ]
        )

    return types.InlineKeyboardMarkup(inline_keyboard=kb)
