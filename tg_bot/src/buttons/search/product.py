from aiogram import types

from src.buttons.search.shops import create_pagination_buttons
from src.callback.search.product import ProductCallback


def create_product_buttons(data: list, shop: dict, offset=0, longitude=None, latitude=None, back_url=None, source=None):
    kb = [
        [
            types.InlineKeyboardButton(
                text=product.get('name'),
                callback_data=ProductCallback(
                    id=product.get('id'),
                    shop_id=shop.get('id')
                ).pack()
            ),
        ] for product in data

    ]
    if data:
        pagination_buttons = create_pagination_buttons(offset, longitude, latitude, back_url, source=source)
        kb.append(pagination_buttons)
    return types.InlineKeyboardMarkup(inline_keyboard=kb)

