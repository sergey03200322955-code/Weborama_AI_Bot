import asyncio
from aiogram import Bot, Dispatcher
from config.settings import settings
from bot.handlers import register_handlers

async def main():
    bot = Bot(token=settings.TG_BOT_TOKEN)
    dp = Dispatcher()

    # регаем хендлеры
    register_handlers(dp)

    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
