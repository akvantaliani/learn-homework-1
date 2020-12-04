"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке
   https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну
   получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt Downloads/telegram-mac.dmg
"""


def main(files_dir):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if files_dir[-1] == '/':
        files_dir = files_dir[:-1]
    try:
        with open(f'{files_dir}/referat.txt', 'r', encoding='utf-8') as file1:
            content = file1.read()
    except FileNotFoundError:
        return f'Файл referat.txt в папке {files_dir} не найден.'
    except UnicodeDecodeError:
        return 'Файл referat.txt не может быть прочтён'
    words_list = content.split()
    words_qty = len(words_list)
    content2 = content.replace('.', '!')
    with open(f'{files_dir}/referat2.txt', 'w', encoding='utf-8') as file2:
        file2.write(content2)
    return words_qty


if __name__ == "__main__":
    f_dir = input('Укажите путь к файлу referat.txt: ')
    print(main(f_dir))
