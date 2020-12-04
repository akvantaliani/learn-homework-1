"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, date, timedelta
import locale


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    locale.setlocale(locale.LC_TIME, 'ru_RU')
    delta_1 = timedelta(days=1)
    delta_30 = timedelta(days=30)
    today_ = date.today()
    today_str = today_.strftime('%d %B %Y года')
    yesterday_ = today_ - delta_1
    yesterday_str = yesterday_.strftime('%d %B %Y года')
    days_ago_30_ = today_ - delta_30
    days_ago_30_str = days_ago_30_.strftime('%d %B %Y года')
    print(f'Сегодня {today_str}')
    print(f'Вчера было {yesterday_str}')
    print(f'30 дней назад было {days_ago_30_str}')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    try:
        datetime_obj = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
        return datetime_obj
    except ValueError:
        return 'Передан неверный формат даты'


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
