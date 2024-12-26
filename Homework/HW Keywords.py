def max_number(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


def empty_function():
    pass


def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    result = max_number(num1, num2)

    print(result)

except ValueError:
    print("Вы ввели не число!")
finally:
    print("Функция max_number выполнена")

try:
    user_input = int(input("Ввод числа: "))
    for num in even_numbers(user_input):
        print(num)
except ValueError:
    print("Вы ввели не число!")
finally:
    print("Функция even_numbers выполнена")


def test_max_number():
    assert max_number (5, 6) == 6 ,'Число не равно 6'
    assert max_number (-6, 6) == 6 , 'Число не равно 6'
    assert max_number (6, 6) == 6  ,'Число не равно 6'

test_max_number()
print("Тесты пройдены!")