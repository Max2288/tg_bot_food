from aiogram.filters.callback_data import CallbackData


class ShopCallback(CallbackData, prefix="shop"):
    id: int


class PaginationCallback(CallbackData, prefix="page"):
    action: str
    offset: int
    longitude: float | None
    latitude: float | None
    back_url: str | None
    source: str | None
