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
    user_input = int(input("Ввод числа:"))
    for num in even_numbers(user_input):
        print(num)
except ValueError:
    print("Вы ввели не число!")
finally:
    print("Завершение программы")


def max_number(a,b):
    if a >= b:
        return a
    else:
        return b

def test_max_number():
    assert max_number(5, 6) == 5

test_max_number()
print("Тесты пройдены!")