def max_number(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    for num in max_number(num1, num2):
        print(num)
except ValueError:
    print("Вы ввели не число!")
finally:
    print("Завершение программы")


def empty_function():
    pass


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
try:
    user_input = int(input("Ввод числа: "))
    for num in even_numbers(user_input):
        print(num)
except ValueError:
    print("Вы ввели не число!")
finally:
    print("Завершение программы")


def test_max_number():
    assert 5 == 5, "Условие теста не выполняется!"
    assert 5 >= 0, "Условие теста не выполняется!"
    assert 5 <= 100, "Условие теста не выполняется!"

test_max_number()
print("Тесты пройдены!")