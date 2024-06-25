from aiogram import types

from src.callback.feedback.feedback import FindFeedback
from src.callback.search.shop import PaginationCallback, ShopCallback


def create_pagination_buttons(
        offset=0, longitude=None, latitude=None, back_url=None, source=None, shop_id: int = None
):
    pg_btns = [
        types.InlineKeyboardButton(
            text="⬅️",
            callback_data=PaginationCallback(
                action="prev",
                offset=max(0, offset - 5),
                longitude=longitude,
                latitude=latitude,
                back_url=back_url,
                source=source,
            ).pack(),
        ),
    ]
    if shop_id:
        pg_btns.append(types.InlineKeyboardButton(
            text="Отзывы",
            callback_data=FindFeedback(shop_id=shop_id).pack(),
        ), )
    pg_btns.append(types.InlineKeyboardButton(
        text="➡️",
        callback_data=PaginationCallback(
            action="next",
            offset=offset + 5,
            longitude=longitude,
            latitude=latitude,
            back_url=back_url,
            source=source,
        ).pack(),
    ), )
    return pg_btns


def create_shop_buttons(
        data: list, offset=0, longitude=None, latitude=None, back_url=None
):
    kb = [
        [
            types.InlineKeyboardButton(
                text=shop.get("name"),
                callback_data=ShopCallback(id=shop.get("id")).pack(),
            ),
        ]
        for shop in data
    ]
    pagination_buttons = create_pagination_buttons(
        offset, longitude, latitude, back_url, source="shop"
    )
    kb.append(pagination_buttons)

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


SHARE_LOC = "Поделиться местоположением"
DEFAULT_LOC = "Искать по всем"


def asq_locations_buttons():
    kb = [
        [types.KeyboardButton(text=SHARE_LOC, request_location=True)],
        [types.KeyboardButton(text=DEFAULT_LOC)],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
