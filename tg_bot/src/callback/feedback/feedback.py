from aiogram.filters.callback_data import CallbackData


class FeedbackCallback(CallbackData, prefix="feedback"):
    shop_id: int


class FindFeedback(CallbackData, prefix="findfb"):
    shop_id: int


class LookFeedback(CallbackData, prefix="lookfb"):
    fb_id: int