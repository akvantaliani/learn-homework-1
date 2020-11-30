# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.
number_list = [1,3,123,42,11,77,5,-42,0,-1]
for number in number_list:
    print(number + 1)

# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.
input_str = input("Введите любую строку: ")
for letter in input_str:
    print(letter)
    
# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.
def main(school_scores):
    school_scores_sum = 0
    for school_class in school_scores:
        class_scores_sum = 0
        for score in school_class['scores']:
            class_scores_sum += score
        class_score_ave = class_scores_sum/len(school_class['scores'])
        class_number = school_class['school_class']
        print(f'Средний балл в {class_number} классе: {round(class_score_ave,1)}')
        school_scores_sum += class_score_ave
    school_score_ave = school_scores_sum/len(school_scores)
    print(f'Средний балл в школе: {round(school_score_ave,1)}')

school1_scores = [
    {'school_class': '4А', 'scores': [4,5,3,3,4]},
    {'school_class': '4Б', 'scores': [3,4,4,3,2]},
    {'school_class': '5А', 'scores': [4,5,5,5,3,5]},
    {'school_class': '6В', 'scores': [2,3,3,2,3,4]},
    {'school_class': '6А', 'scores': [5,3,4,5,2,3]},
    {'school_class': '11Б', 'scores': [5,4,3]},
    {'school_class': '10Д', 'scores': [4,5,3,2,2,2]},
    {'school_class': '7Г', 'scores': [5,4,3,5,4,3]},
    {'school_class': '3А', 'scores': [5,5,5,4,5,5,5,4,5,3,5]},
    {'school_class': '8Б', 'scores': [4,3,5,3,4,4,3,]},
    {'school_class': '9А', 'scores': [4,5,5,4,3,5,2,5]},
]   
if __name__ == "__main__":
    main(school1_scores)
