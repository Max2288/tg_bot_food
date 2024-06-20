from aiogram.fsm.state import State, StatesGroup


class SearchState(StatesGroup):
    get_location = State()
    find_shop = State()
    find_product = State()

