from conf.config import settings
from src.buttons.main.back import get_back_button
from src.callback.search.product import ProductCallback
from src.handlers.search import search_router
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiohttp import ClientResponseError
from aiogram.fsm.context import FSMContext
from src.utils.request import do_request


def prepare_product_data(data: dict) -> str:
    field_names = ['Название', 'Количество', 'Цена']
    product = "\n".join(
        "%s: %s" % (name, val) for name, val in zip(
            field_names, [data.get('name'), data.get('quantity'), data.get('price')]
        )
    )
    return product


@search_router.callback_query(ProductCallback.filter())
async def handle_product_callback(callback_query: CallbackQuery, callback_data: ProductCallback, state: FSMContext):
    await callback_query.message.delete()
    try:
        data = await do_request(
            f'{settings.TINDER_BACKEND_HOST}/api/v1/product/{callback_data.id}',
            method='GET',
        )
        await callback_query.message.answer_photo(
            photo='https://www.souz-pribor.ru/upload/iblock/087/MI-3123-Smartec.jpeg',
            # потом должно быть data.get('image')
            caption=prepare_product_data(data),
            reply_markup=get_back_button(previous_id=callback_data.shop_id)
        )
        await state.set_state(None)
    except ClientResponseError:
        await callback_query.message.answer('Произошла ошибка при получении продуктов.')
    await callback_query.answer()
