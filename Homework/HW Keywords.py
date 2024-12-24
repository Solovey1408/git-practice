def max_number(a, b):
    if a > b:
        return a
    else:
        return b

def empty_function():
    pass

print("Функция определена, но пока ничего не делает.")

def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

even_numbers(10)