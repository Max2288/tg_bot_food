from typing import Callable, ParamSpec

from aiogram import types


P = ParamSpec('P')

SETTINGS_FOR_NOTIFICATIONS = 'Настройка уведомлений'
REVIEWS_AND_MARKS = 'Отзывы и оценки'
FIND_BTN = 'Найти'
NEWS_AND_ACTIONS = 'Новости и акции'
SUPPORT_BTN = 'Служба поддержки'


def get_main_keyboard(role: str = 'user', **kwargs) -> types.ReplyKeyboardMarkup:
    return role_to_keyboard_getter[role](**kwargs)


def _get_keyboard_user(**kwargs) -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text=SETTINGS_FOR_NOTIFICATIONS)],
        [types.KeyboardButton(text=REVIEWS_AND_MARKS)],
        [types.KeyboardButton(text=FIND_BTN)],
        [types.KeyboardButton(text=NEWS_AND_ACTIONS)],
        [types.KeyboardButton(text=SUPPORT_BTN)],
    ]

    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def _get_keyboard_admin(**kwargs) -> types.ReplyKeyboardMarkup:
    kb = [
        [types.KeyboardButton(text='')],
    ]

    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


role_to_keyboard_getter: dict[str, Callable[[P.kwargs], types.ReplyKeyboardMarkup]] = {
    'user': _get_keyboard_user,
    'admin': _get_keyboard_admin,
}