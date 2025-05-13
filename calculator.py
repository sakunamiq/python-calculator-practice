# calculator.py

def add(x, y):
    """Эта функция складывает два числа"""
    return x + y

def subtract(x, y):
    """Эта функция вычитает второе число из первого"""
    return x - y

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print(f"{num1} + {num2} = {add(num1, num2)}")
    # Ожидаемый результат: 10 + 5 = 15

    num3 = 20
    num4 = 7
    print(f"{num3} - {num4} = {subtract(num3, num4)}")
    # Ожидаемый результат: 20 - 7 = 13