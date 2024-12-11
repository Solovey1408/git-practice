try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    result = num1 / num2

except ValueError:
    print("Введите число!")
except ZeroDivisionError:
    print("Деление на ноль!")
else:
    print(f"Результат: {result}")
finally:
    print("Завершение работы программы")