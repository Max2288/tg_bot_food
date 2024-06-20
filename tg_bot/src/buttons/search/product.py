from aiogram import types

from src.callback.search.product import ProductCallback


def create_product_buttons(data: list, shop: dict):
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
    return types.InlineKeyboardMarkup(inline_keyboard=kb)

