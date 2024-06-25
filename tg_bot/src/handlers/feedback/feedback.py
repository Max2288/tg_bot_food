from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from src.buttons.feedback.feedback import get_feedback_buttons
from src.buttons.main.default import create_star_buttons
from src.callback.feedback.feedback import FeedbackCallback, FindFeedback, LookFeedback
from src.handlers.feedback.router import feedback_router
from src.middleware.auth import access_token_cxt
from src.states.main import FeedbackStates
from src.utils.request import do_request


@feedback_router.callback_query(FeedbackCallback.filter())
async def handle_feedback_callback(
    callback_query: CallbackQuery, callback_data: FeedbackCallback, state: FSMContext
):
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
    rating = int(callback_query.data.split("_")[1])
    user_data = await state.get_data()
    feedback_text = user_data["feedback_text"]
    back_url = f'api/v1/feedback/{user_data.get("shop_id")}'
    params = {"score": rating, "description": feedback_text}
    headers = {"auth": f"Bearer {access_token_cxt.get()}"}
    _, status = await do_request(
        back_url, method="post", params=params, headers=headers
    )
    await callback_query.message.answer(
        f"Спасибо за ваш отзыв!\nТекст: {feedback_text}\nРейтинг: {rating} ⭐"
    )
    await state.clear()


@feedback_router.callback_query(FindFeedback.filter())
async def find_feedback_for_shop(callback_query: CallbackQuery, callback_data: FindFeedback):
    shop_id = callback_data.shop_id
    back_url = f'api/v1/feedback/{shop_id}'
    headers = {"auth": f"Bearer {access_token_cxt.get()}"}
    feedbacks, _ = await do_request(
        back_url, method="get", headers=headers
    )
    await callback_query.message.answer(text='Отзывы:', reply_markup=get_feedback_buttons(feedbacks, source='feedback', back_url=back_url))


@feedback_router.callback_query(LookFeedback.filter())
async def look_feedback_info(callback_query: CallbackQuery, callback_data: LookFeedback):
    back_url = f'api/v1/feedback/fb/{callback_data.fb_id}'
    headers = {"auth": f"Bearer {access_token_cxt.get()}"}
    feedback_info, _ = await do_request(
        back_url, method="get", headers=headers
    )
    raiting_table = {
        i : i*'⭐' for i in range(1, 6)
    }
    user_hidden = str(feedback_info.get("user"))[:4] + "*" * (len(str(feedback_info.get("user"))) - 4)
    user_score = raiting_table[feedback_info.get("score")]
    await callback_query.message.answer(
        text=f'Отзыв по этому магазину от пользователя {user_hidden} :\nОценка: {user_score}\nОписание: {feedback_info.get("description")}'
    )