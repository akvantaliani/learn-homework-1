import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
from bot_start import greet_user
from bot_answers import talk_to_me

logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()


# Вызываем функцию main() - именно эта строчка запускает бота
if __name__ == "__main__":
    main()
