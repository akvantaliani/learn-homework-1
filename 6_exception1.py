# Перепишите функцию hello_user() из задания про while, чтобы она перехватывала KeyboardInterrupt,
# писала пользователю "Пока!" и завершала работу при помощи оператора break

def hello_user():
    user_input = ""
    while user_input != "Хорошо":
        try:
            user_input = input("Как дела?\n")
        except KeyboardInterrupt:
            print(" Пока!")
            break
    
if __name__ == "__main__":
    hello_user()
