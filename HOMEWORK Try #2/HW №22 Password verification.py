# Заведите в коде программы переменную и поместите в неё какой-нибудь не настоящий текстовый пароль.
user_password = '123qwerty456'
# Далее в цикле запрашивайте у пользователя ввод пароля. Если введенный пароль совпал с заданным в коде ранее,
# то пользователю следует об этом сообщить и завершить цикл. Иначе перейти к следующей итерации-попытке.Программа должна
# быть реализована с помощью цикла while.

in_password = str(input("Введите пароль: "))

while in_password == user_password:
    print("Пароль принят!")
    break
while in_password != user_password:
    print("Пароль не верный!")
    break