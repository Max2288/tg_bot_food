from aiogram import types

from src.callback.search.shop import ShopCallback


def create_shop_buttons(data: list):
    kb = [
        [
            types.InlineKeyboardButton(
                text=shop.get('name'),
                callback_data=ShopCallback(
                    id=shop.get('id')
                ).pack()
            ),
        ] for shop in data
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


SHARE_LOC = 'Поделиться местоположением'
DEFAULT_LOC = 'Искать по всем'

def asq_locations_buttons():
    kb = [
        [types.KeyboardButton(text=SHARE_LOC, request_location=True)],
        [types.KeyboardButton(text=DEFAULT_LOC)]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)