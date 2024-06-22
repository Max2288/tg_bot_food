from aiogram.fsm.context import FSMContext
from aiogram import types

from src.buttons.main.default import create_star_buttons
from src.callback.feedback.feedback import FeedbackCallback

from src.handlers.feedback.router import feedback_router

from aiogram.types import CallbackQuery

from src.middleware.auth import access_token_cxt
from src.states.main import FeedbackStates
from src.utils.request import do_request


@feedback_router.callback_query(FeedbackCallback.filter())
async def handle_feedback_callback(callback_query: CallbackQuery, callback_data: FeedbackCallback, state: FSMContext):
    await state.update_data(shop_id=callback_data.shop_id)
    await callback_query.message.answer("Пожалуйста, введите текст вашего отзыва:")
    await state.set_state(FeedbackStates.waiting_for_feedback_text)


@feedback_router.message(FeedbackStates.waiting_for_feedback_text)
async def feedback_text_received(message: types.Message, state: FSMContext):
    await state.update_data(feedback_text=message.text)
    kb = create_star_buttons()
    await message.answer("Пожалуйста, выберите рейтинг от 1 до 5:", reply_markup=kb)
    await state.set_state(FeedbackStates.waiting_for_rating)


@feedback_router.callback_query(FeedbackStates.waiting_for_rating)
async def rating_received(callback_query: CallbackQuery, state: FSMContext):
    rating = int(callback_query.data.split('_')[1])
    user_data = await state.get_data()
    feedback_text = user_data['feedback_text']
    back_url = f'api/v1/feedback/{user_data.get("shop_id")}'
    params = {
        "score": rating,
        "description": feedback_text
    }
    headers = {
        'auth': f'Bearer {access_token_cxt.get()}'
    }
    _, status = await do_request(back_url, method='post', params=params, headers=headers)
    await callback_query.message.answer(f"Спасибо за ваш отзыв!\nТекст: {feedback_text}\nРейтинг: {rating} ⭐")
    await state.clear()