# Установите модуль ephem
# Добавьте в бота команду /planet, которая будет принимать на вход название планеты
# на английском, например /planet Mars
# В функции-обработчике команды из update.message.text получите
# название планеты (подсказка: используйте .split())
# При помощи условного оператора if и ephem.constellation научите бота отвечать,
# в каком созвездии сегодня находится планета.
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from datetime import date

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def find_planet(update, context):
    user_text = update.message.text.split()
    if len(user_text) > 1:
        today_str = date.today().strftime("%Y/%m/%d")
        planet_input = user_text[1].capitalize()
        try:
            planet_class = getattr(ephem, planet_input)
            planet_today = planet_class(today_str)
            constellation_tuple = ephem.constellation(planet_today)
            constellation = constellation_tuple[1]
            constellation_to_reply = f'{planet_input} находится в созвездии "{constellation}".'
            print(constellation_to_reply)
            update.message.reply_text(constellation_to_reply)
        except AttributeError:
            wrong_planet = f'Я не знаю небесное тело с названием "{planet_input}".'
            print(wrong_planet)
            update.message.reply_text(wrong_planet)
    else:
        empty_planet_reply = 'Вы не назвали небесное тело.'
        print(empty_planet_reply)
        update.message.reply_text(empty_planet_reply)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", find_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
