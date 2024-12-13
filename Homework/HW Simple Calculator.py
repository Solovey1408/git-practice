def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
        message = "Выберите математическую операцию: "

        correct_operations = '+-/*'
        operation = input(message)
        result = ' '
        while operation not in correct_operations:
            print('Такая операция недоступна.Повторите попытку.')
            operation = input(message)
        if operation == '+':
            print('Сложение')
            result = num1 + num2
        elif operation == '-':
            print('Вычитание')
            result = num1 - num2
        elif operation == '/':
            print('Деление')
            result = num1 / num2
        elif operation == '*':
            print('Умножение')
            result = num1 * num2
        else:
            print('Неизвестная операция')
    except ZeroDivisionError:
        print("Деление на ноль запрещено")
    except ValueError:
        print("Введите число!")
    else:
        print(f"Результат: {result}")
    finally:
        print("Завершение работы программы")


calculator()
calculator()
calculator()
calculator()