user_password = '123qwerty456'

in_password = ""

while in_password != user_password:
    in_password = str(input("Введите пароль: "))
    if in_password != user_password:
        print("Пароль не верный!")

if in_password == user_password:
    print("Пароль принят!")

