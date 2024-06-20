from aiogram.filters.callback_data import CallbackData


class BackCallback(CallbackData, prefix="back"):
    previous_id: int
