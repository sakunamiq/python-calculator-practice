# calculator.py

def add(x, y):
    """Эта функция складывает два числа"""
    return x + y

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print(f"{num1} + {num2} = {add(num1, num2)}")
    # Ожидаемый результат: 10 + 5 = 15