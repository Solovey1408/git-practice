try:
    user_num_1 = float(input("Введите первое число: "))
    user_num_2 = float(input("Введите второе число: "))

    message = "Выберите математическую операцию"

    correct_operations = '+-/*'

    operation = input(message)

    while operation not in correct_operations:
        print('Такая операция недоступна.Повторите попытку.')
        operation = input(message)
    if operation == '+':
        print('Сложение')
        result = user_num_1 + user_num_2
    elif operation == '-':
        print('Вычитание')
        result = user_num_1 - user_num_2
    elif operation == '/':
        print('Деление')
        result = user_num_1 / user_num_2
    elif operation == '*':
        print('Умножение')
        result = user_num_1 * user_num_2
    else:
        print('Неизвестная операция')
except ZeroDivisionError:
    print("Деление на ноль запрещено")
except ValueError:
    print("Вы ввели не число!")
else:
    print(f"Результат: {result}")
finally:
    print("Завершение работы программы")
