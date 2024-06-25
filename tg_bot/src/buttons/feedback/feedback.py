from aiogram import types
from src.buttons.search.shops import create_pagination_buttons
from src.callback.feedback.feedback import LookFeedback


def get_feedback_buttons(
    feedbacks: list[dict],
    offset=0,
    back_url=None,
    source=None,
    longitude = None,
    latitude = None
):
    kb = [
        [
            types.InlineKeyboardButton(
                text=feedback.get("description")[:20],
                callback_data=LookFeedback(
                    fb_id=feedback.get("id")
                ).pack(),
            ),
        ]
        for feedback in feedbacks
    ]
    if feedbacks:
        pagination_buttons = create_pagination_buttons(
            offset, longitude, latitude, back_url, source=source
        )
        kb.append(pagination_buttons)
    return types.InlineKeyboardMarkup(inline_keyboard=kb)
