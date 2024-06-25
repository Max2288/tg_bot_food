from urllib.parse import urlencode

from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import BufferedInputFile, CallbackQuery
from aiohttp import ClientResponseError
from conf.config import settings
from src.buttons.feedback.feedback import get_feedback_buttons
from src.buttons.main.default import FIND_BTN, get_main_keyboard, SUPPORT_BTN
from src.buttons.search.product import create_product_buttons
from src.buttons.search.shops import asq_locations_buttons, create_shop_buttons
from src.callback.search.shop import PaginationCallback, ShopCallback
from src.handlers.search.router import search_router
from src.states.main import SearchState
from src.utils.minio import get_file_from_minio, get_input_file
from src.utils.request import do_request


@search_router.message(F.text == SUPPORT_BTN)
async def give_support(message: types.Message) -> None:
    await message.answer(
        "По всем вопросам можете обращаться к @maxbzb",
    )


@search_router.message(F.text == FIND_BTN)
async def find_shop(message: types.Message, state: FSMContext) -> None:
    await message.answer(
        "Пожалуйста, отправьте ваше местоположение.",
        reply_markup=asq_locations_buttons(),
    )
    await state.set_state(SearchState.get_location)
    return


@search_router.message(SearchState.get_location)
async def handle_location(message: types.Message, state: FSMContext) -> None:
    shop_url = f"api/v1/search/shop"
    initial_shop_url = shop_url
    longitude = None
    latitude = None
    if message.location:
        location = message.location
        latitude = location.latitude
        longitude = location.longitude
        shop_url += f"?latitude={latitude}&longitude={longitude}"
    try:
        data, _ = await do_request(shop_url, method="GET")
        await state.set_state(SearchState.find_shop)
        await message.answer("Обрабатываю...", reply_markup=get_main_keyboard())
        await message.answer(
            "Выберите магазин:",
            reply_markup=create_shop_buttons(
                data, 0, longitude, latitude, initial_shop_url
            ),
        )
    except ClientResponseError as e:
        await message.answer(f"Произошла ошибка при поиске магазинов. {e}")


async def prepare_shop_caption(shop: dict, count_products: int) -> str:
    return "Название магазина: %s\nОписание: %s\n%s" % (
        shop.get("name"),
        shop.get("description"),
        (
            "Продукты для этого магазина:"
            if count_products
            else "Продукты для этого магазина отсутствуют"
        ),
    )


@search_router.callback_query(ShopCallback.filter())
async def handle_shop_callback(
    callback_query: CallbackQuery, callback_data: ShopCallback, state: FSMContext
):
    try:
        back_url = f"api/v1/shop/{callback_data.id}"
        data, _ = await do_request(back_url, method="get")
        shop = data.get("shop")
        products = data.get("products")
        input_file = await get_input_file(shop.get("image"))
        caption = await prepare_shop_caption(shop, products)
        await callback_query.message.answer_photo(
            photo=input_file,
            caption=caption,
            reply_markup=create_product_buttons(
                products, shop, offset=0, back_url=back_url
            ),
        )
        await state.set_state(SearchState.find_product)
    except ClientResponseError as e:
        await callback_query.message.answer(
            "Произошла ошибка при поиске магазинов. {}".format(e)
        )
    await callback_query.answer()


async def prepare_shop_from_callback(url, latitude=None, longitude=None, offset=None):
    params = {}

    if latitude is not None:
        params["latitude"] = latitude
    if longitude is not None:
        params["longitude"] = longitude
    if offset is not None:
        params["offset"] = offset
    query_string = urlencode(params)
    return f"{url}?{query_string}"


@search_router.callback_query(PaginationCallback.filter())
async def handle_pagination(
        callback_query: types.CallbackQuery,
        callback_data: PaginationCallback,
        state: FSMContext,
):
    offset = int(callback_data.offset)
    shop_url = await prepare_shop_from_callback(
        callback_data.back_url, callback_data.latitude, callback_data.longitude, offset
    )
    try:
        shops, _ = await do_request(shop_url, method="GET")
        await state.update_data(offset=offset)
        reply_markup = None
        match callback_data.source:
            case "shop":
                reply_markup = create_shop_buttons(
                    shops,
                    offset,
                    callback_data.longitude,
                    callback_data.latitude,
                    back_url=callback_data.back_url,
                )
            case "feedback":
                reply_markup = get_feedback_buttons(
                    shops,
                    offset=offset,
                    back_url=callback_data.back_url,
                    source=callback_data.source
                )
            case _:
                reply_markup = create_product_buttons(
                    shops.get("products"),
                    shops.get("shop"),
                    offset=offset,
                    back_url=callback_data.back_url,
                )

        await callback_query.message.edit_reply_markup(reply_markup=reply_markup)

    except ClientResponseError:
        await callback_query.message.answer(
            "Произошла ошибка при обновлении списка магазинов."
        )

