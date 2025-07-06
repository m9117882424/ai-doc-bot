from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from aiogram.client.telegram import TelegramAPIServer
from aiogram.utils import executor
from config import BOT_TOKEN, TG_API_URL
from handlers.multi_doc_handler import register_handlers as register_multi

def setup_bot():
    if "localhost" in TG_API_URL:
        server = TelegramAPIServer.from_base(TG_API_URL)
        bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML, server=server)
    else:
        bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    return bot

def main():
    bot = setup_bot()
    dp = Dispatcher(bot)
    register_multi(dp)
    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()