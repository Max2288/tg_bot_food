from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiohttp import ClientResponseError

from src.buttons.main.back import get_feedback_with_back_buttons
from src.callback.search.product import ProductCallback
from src.handlers.search.router import search_router
from src.utils.minio import get_input_file
from src.utils.request import do_request


def prepare_product_data(data: dict) -> str:
    field_names = ["Название", "Количество", "Цена"]
    product = "\n".join(
        "%s: %s" % (name, val)
        for name, val in zip(
            field_names, [data.get("name"), data.get("quantity"), data.get("price")]
        )
    )
    return product


@search_router.callback_query(ProductCallback.filter())
async def handle_product_callback(
    callback_query: CallbackQuery, callback_data: ProductCallback, state: FSMContext
):
    print('ТУТ МЫ')
    await callback_query.message.delete()
    try:
        product, _ = await do_request(
            f"api/v1/product/{callback_data.id}",
            method="GET",
        )
        input_file = await get_input_file(product.get("image"))
        await callback_query.message.answer_photo(
            photo=input_file,
            caption=prepare_product_data(product),
            reply_markup=get_feedback_with_back_buttons(
                previous_id=callback_data.shop_id
            ),
        )
        await state.set_state(None)
    except ClientResponseError:
        await callback_query.message.answer("Произошла ошибка при получении продуктов.")
    await callback_query.answer()
