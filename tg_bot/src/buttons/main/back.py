from aiogram import types
from src.callback.feedback.feedback import FeedbackCallback
from src.callback.main.back import BackCallback


def get_back_button(previous_id: int):
    kb = [
        [
            types.InlineKeyboardButton(
                text="Назад", callback_data=BackCallback(previous_id=previous_id).pack()
            ),
        ]
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def get_feedback_with_back_buttons(previous_id: int) -> types.InlineKeyboardMarkup:
    kb = [
        [
            types.InlineKeyboardButton(
                text="Оставить отзыв",
                callback_data=FeedbackCallback(shop_id=previous_id).pack(),
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Назад", callback_data=BackCallback(previous_id=previous_id).pack()
            ),
        ],
    ]

    return types.InlineKeyboardMarkup(inline_keyboard=kb)
