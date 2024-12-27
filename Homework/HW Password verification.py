correct_pass = "qwer123"

while True:
    in_password = str(input("Введите пароль: "))
    if correct_pass == in_password:
        print("Пароль верный")
        break
    else:
        print('Пароль не верный')