from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.buttons.main.back import get_back_button
from src.buttons.search.product import create_product_buttons
from src.callback.main.back import BackCallback
from src.handlers.main.router import main_router
from src.handlers.search.find_product import prepare_product_data
from src.states.main import SearchState
from src.utils.request import do_request
from aiogram.types import CallbackQuery, InputMediaPhoto


@main_router.callback_query(BackCallback.filter())
async def handle_back_callback(callback_query: CallbackQuery, callback_data: BackCallback, state: FSMContext):
    await state.set_state(SearchState.find_shop)
    previous_data = await do_request(
            f'{settings.TINDER_BACKEND_HOST}/api/v1/shop/{callback_data.previous_id}',
            method='GET',
    )
    shop = previous_data.get('shop')
    products = previous_data.get('products')
    media = InputMediaPhoto(
        media='https://i.sstatic.net/5l6Qz.png', #TODO ЗДЕСЬ ДОЛЖНО БЫТЬ SHOP IMAGE
        caption='Название магазина: %s\nОписание: %s\nПродукты для этого магазина:' % (
            shop.get('name'), shop.get('description')
        )
    )

    await callback_query.message.edit_media(
        media=media,
        reply_markup=create_product_buttons(products, shop)
    )