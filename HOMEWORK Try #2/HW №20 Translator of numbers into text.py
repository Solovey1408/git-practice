# Напишите программу, которая принимает на ввод целое число в диапазоне от 1 до 5,
# и выводит соответствующее ему слово на английском языке.
try:
    user_number = int(input("Введите число от 1 до 5: "))

    if user_number == 1:
        print('One')

    if user_number == 2:
        print('Two')

    if user_number == 3:
        print('Three')

    if user_number == 4:
        print('Four')

    if user_number == 5:
        print('Five')

    if user_number > 5:
        print('Число отсутствует в интервале допустимых значений')

except ValueError:
    print("Вы ввели не число!")

finally:
    print("Завершение работы программы")