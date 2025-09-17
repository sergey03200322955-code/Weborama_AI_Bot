from aiogram import Router, types
from services.gpt_service import ask_gpt
from storage.history_repository import save_message, get_history

router = Router()

def register_handlers(dp):
    dp.include_router(router)

@router.message(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой менеджер-бот. Пиши вопрос, я попробую ответить 😉")

@router.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    # сохраняем запрос
    save_message(user_id, "user", text)

    # получаем историю
    history = get_history(user_id)

    # спрашиваем GPT
    answer = ask_gpt(history)

    # сохраняем ответ
    save_message(user_id, "bot", answer)

    await message.answer(answer)
