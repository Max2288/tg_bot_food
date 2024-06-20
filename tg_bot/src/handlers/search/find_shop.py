from aiogram import types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiohttp import ClientResponseError

from src.buttons.main.default import FIND_BTN, get_main_keyboard
from src.buttons.search.product import create_product_buttons
from src.buttons.search.shops import create_shop_buttons, asq_locations_buttons
from src.callback.search.shop import ShopCallback
from src.handlers.search.router import search_router
from src.states.main import SearchState
from src.utils.request import do_request

from conf.config import settings


@search_router.message(F.text == FIND_BTN)
async def find_shop(message: types.Message, state: FSMContext) -> None:
    await message.answer('Пожалуйста, отправьте ваше местоположение.', reply_markup=asq_locations_buttons())
    await state.set_state(SearchState.get_location)
    return


@search_router.message(SearchState.get_location)
async def handle_location(message: types.Message, state: FSMContext) -> None:
    shop_url = f'{settings.TINDER_BACKEND_HOST}/api/v1/search/shop'
    if message.location:
        location = message.location
        latitude = location.latitude
        longitude = location.longitude
        shop_url += f'?latitude={latitude}&longitude={longitude}'
    try:
        data = await do_request(shop_url, method='GET')
        await state.set_state(SearchState.find_shop)
        await message.answer('Обрабатываю...', reply_markup=get_main_keyboard())
        await message.answer('Выберите магазин:', reply_markup=create_shop_buttons(data))
    except ClientResponseError:
        await message.answer('Произошла ошибка при поиске магазинов.')


@search_router.callback_query(ShopCallback.filter())
async def handle_shop_callback(callback_query: CallbackQuery, callback_data: ShopCallback, state: FSMContext):
    try:
        data = await do_request(f'{settings.TINDER_BACKEND_HOST}/api/v1/shop/{callback_data.id}', method='GET')
        shop = data.get('shop')
        products = data.get('products')
        await state.set_state(SearchState.find_product)
        await callback_query.message.answer_photo(
            photo='https://i.sstatic.net/5l6Qz.png',#TODO потом должно быть shop.get('image')
            caption=f'Название магазина: {shop.get("name")}\nОписание: {shop.get("description")}\nПродукты для этого магазина:',
            reply_markup=create_product_buttons(products, shop)
        )
    except ClientResponseError:
        await callback_query.message.answer('Произошла ошибка при поиске магазинов.')
    await callback_query.answer()
