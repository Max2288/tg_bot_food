from aiogram.fsm.state import State, StatesGroup


class SearchState(StatesGroup):
    get_location = State()
    find_shop = State()
    find_product = State()


class FeedbackStates(StatesGroup):
    shop_id = State()
    waiting_for_feedback_text = State()
    waiting_for_rating = State()
