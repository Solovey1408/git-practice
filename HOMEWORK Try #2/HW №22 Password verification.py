user_password = '123qwerty456' #есть пароль с которым мы должны свериться

def input_password():

    while in_password != user_password:
        print("Пароль не верный!")
        in_password = str(input("Введите пароль: "))


    if in_password == user_password:
        print("Пароль принят!")
