# Напишите программу, которая вычисляет сумму всех четных чисел от 1 до 100.
def sum_of_even(a, b):
    even_sum = 0
    for i in range(a, b):
        if i % 2 == 0:
            even_sum += i
    return even_sum


# Создайте список, содержащий квадраты всех нечетных чисел от 1 до 10, используя генератор списка.
def square_odd_numbers(a, b):
    square_odd = [i ** 2 for i in range(a, b) if i % 2 != 0]
    return square_odd


# Напишите программу, которая просит пользователя ввести число и продолжает запрашивать числа, пока
# пользователь не введет отрицательное число. Затем программа должна вывести количество введенных чисел.
def input_numbers():
    count = 0 #счетчик
    user_number = 0 #заглушка

    while user_number >= 0:
        user_number = int(input("Введите число: "))
        if user_number >= 0: #
            count += 1

    return count


sum_even_numbers = sum_of_even(0,101)
print(sum_even_numbers)
sq_od_num = square_odd_numbers(0, 10)
print(sq_od_num)
count_all_input = input_numbers()
print(count_all_input)