def main(age):
    if 3 <= age < 7:
        return "Вы ходите в деткий сад."
    elif 7 <= age < 18:
        return "Вы учитесь в школе."
    elif 18 <= age < 23:
        return "Вы учитесь в ВУЗе."
    elif 23 <= age:
        return "Вы работаете."
    else:
        return "Вы слишком малы, чтобы ввести свой возраст :)"

age_input = int(input("Введите ваш возраст: "))
if __name__ == "__main__":
    kind_of_activity = main(age_input)
    print (kind_of_activity)