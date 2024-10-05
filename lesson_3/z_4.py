def my_func_1(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            raise ValueError
        return x**y

    except Exception:
        return 'Ошибка введённых данных'


def my_func_2(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0 or y >= 0:
            raise ValueError

        fract = len(str(x))
        fract -= len(str(int(x)))
        fract = int(f'1{"0"*fract}')

        x = int(x * fract)
        a = x
        b = fract

        for i in range(abs(y) - 1):
            a *= x
            b *= fract

        return b / a
    except Exception:
        return 'Ошибка введённых данных'


try:
    x, y = input(
        'Введите действительное положительное число x и целое отрицательное число y через пробел\n' # noqa
    ).split()

    print(my_func_1(x, y))
    print(my_func_2(x, y))

except Exception:
    print('Ошибка введённых данных')
