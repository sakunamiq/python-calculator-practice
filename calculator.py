# calculator.py

def add(x, y):
    """Эта функция складывает два числа"""
    return x + y

def subtract(x, y):
    """Эта функция вычитает второе число из первого"""
    return x - y

def multiply(x, y):
    """Эта функция умножает два числа"""
    return x * y

def divide(x, y):
    """Эта функция делит первое число на второе.
    Обрабатывает деление на ноль."""
    if y == 0:
        return "Ошибка: Деление на ноль невозможно!"
    return x / y

if __name__ == "__main__":
    # Примеры для сложения
    num1_add = 10
    num2_add = 5
    print(f"{num1_add} + {num2_add} = {add(num1_add, num2_add)}")

    # Примеры для вычитания
    num1_sub = 20
    num2_sub = 7
    print(f"{num1_sub} - {num2_sub} = {subtract(num1_sub, num2_sub)}")

    # Примеры для умножения
    num1_mul = 6
    num2_mul = 4
    print(f"{num1_mul} * {num2_mul} = {multiply(num1_mul, num2_mul)}")

    # Примеры для деления
    num1_div = 100
    num2_div = 5
    print(f"{num1_div} / {num2_div} = {divide(num1_div, num2_div)}")
    # Ожидаемый результат: 100 / 5 = 20.0

    num3_div = 9
    num4_div = 2
    print(f"{num3_div} / {num4_div} = {divide(num3_div, num4_div)}")
    # Ожидаемый результат: 9 / 2 = 4.5

    num5_div = 7
    num6_div = 0
    print(f"{num5_div} / {num6_div} = {divide(num5_div, num6_div)}")
    # Ожидаемый результат: Ошибка: Деление на ноль невозможно!