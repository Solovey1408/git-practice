# 1. Создайте функцию max_number(a, b), которая принимает два числа и возвращает наибольшее из них.
# Используйте return для возврата результата. В функции не должно быть встроенной функции max().
# Инициализация (объявление) функции
def max_number(a,b):
    if a >= b: #Условие при котором, идёт сравнение числа величины чисел а и b в зависимости друг от друга
        return a #Возврат числа 'а', если оно больше 'b'
    else: #В противном случае
        return b #Возврат числа 'b', если оно больше 'a'


# 2. Определите функцию empty_function(), которая ничего не делает. Используйте pass в качестве тела функции.
# Инициализация (объявление) функции
def empty_function():
    pass  # Код будет добавлен позже


# 3. Напишите функцию even_numbers(n) , которая генерирует все четные числа от 0 до n включительно.
# Используйте yield для возврата каждого четного числа по очереди.
# Инициализация (объявление) функции
def even_numbers(n):
    result = n % 2 #Выполняется деление принятого аргумента на ноль
    if result == 0: #условие если результат деления равен нулю
        yield n
    result = (n + 1) % 2
    if result == 0: #условие если результат деления равен нулю
        yield n


# 4. Напишите автотест для функции max_number(a, b), созданной в первом задании. Убедитесь, что она возвращает правильные
# значения для различных пар чисел. Используйте assert для проверки условий.
# - Дополнительно, добавьте проверку, что функция правильно работает при передаче одинаковых чисел.
assert max_number(5,6)
assert max_number(5,5)
assert max_number(6,5)

even_numbers(10)