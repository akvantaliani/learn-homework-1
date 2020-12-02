"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями
   по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def export_csv(people_list):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('export.csv', 'w', encoding='utf-8', newline='') as csv_file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f=csv_file, fieldnames=fields, delimiter=';')
        writer.writeheader()
        gen = (info_dict for info_dict in people_list)
        for human in gen:
            if human:
                try:
                    info_list = {}
                    info_list['name'] = human.get('name', None)
                    info_list['age'] = human.get('age', None)
                    info_list['job'] = human.get('job', None)
                    writer.writerow(info_list)
                except AttributeError:
                    print(f'"{human}" не является словарём')
            else:
                continue


if __name__ == "__main__":
    workers_list = [
        {'name': 'Joe Malto', 'age': 30, 'job': 'engineer'},
        {'name': 'Terry Dallas', 'age': 33, 'job': 'programmer'},
        {'name': 'Kate Brown', 'age': 29, 'job': 'actress'},
        {'name': 'Anna Marana', 'age': 22, 'job': 'vet'},
        {'name': 'Bill Kogan', 'age': 66, 'job': 'postman'},
    ]
    export_csv(workers_list)
