from aiogram.fsm.context import FSMContext

from conf.config import settings
from src.buttons.main.back import get_back_button
from src.buttons.search.product import create_product_buttons
from src.callback.main.back import BackCallback
from src.handlers.main.router import main_router
from src.handlers.search.find_product import prepare_product_data
from src.states.main import SearchState
from src.utils.minio import get_input_file
from src.utils.request import do_request
from aiogram.types import CallbackQuery, InputMediaPhoto


@main_router.callback_query(BackCallback.filter())
async def handle_back_callback(callback_query: CallbackQuery, callback_data: BackCallback, state: FSMContext):
    await state.set_state(SearchState.find_shop)
    previous_data, _ = await do_request(
            f'api/v1/shop/{callback_data.previous_id}',
            method='GET',
    )
    shop = previous_data.get('shop')
    products = previous_data.get('products')
    input_file = await get_input_file(shop.get('image'))
    media = InputMediaPhoto(
        media=input_file,
        caption='Название магазина: %s\nОписание: %s\nПродукты для этого магазина:' % (
            shop.get('name'), shop.get('description')
        )
    )

    await callback_query.message.edit_media(
        media=media,
        reply_markup=create_product_buttons(products, shop)
    )