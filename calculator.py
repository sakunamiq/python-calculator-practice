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

if __name__ == "__main__":
    # Примеры для сложения
    num1_add = 10
    num2_add = 5
    print(f"{num1_add} + {num2_add} = {add(num1_add, num2_add)}")
    # Ожидаемый результат: 10 + 5 = 15

    # Примеры для вычитания
    num1_sub = 20
    num2_sub = 7
    print(f"{num1_sub} - {num2_sub} = {subtract(num1_sub, num2_sub)}")
    # Ожидаемый результат: 20 - 7 = 13

    # Примеры для умножения
    num1_mul = 6
    num2_mul = 4
    print(f"{num1_mul} * {num2_mul} = {multiply(num1_mul, num2_mul)}")
    # Ожидаемый результат: 6 * 4 = 24

    num3_mul = 7
    num4_mul = 0
    print(f"{num3_mul} * {num4_mul} = {multiply(num3_mul, num4_mul)}")
    # Ожидаемый результат: 7 * 0 = 0