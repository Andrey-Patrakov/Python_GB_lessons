import traceback


class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a, b = [float(i) for i in input("Введите 2 числа: ").split()]
    if b == 0:
        raise MyZeroDivisionError("Деление на 0")
    print(a / b)

except Exception as e:
    print(f"Ошибка: {e}\n {traceback.format_exc()}")
