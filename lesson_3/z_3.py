def my_func(a, b, c):
    s_list = sorted([a, b, c], reverse=True)
    return sum(s_list[:2:])


try:
    a, b, c = list(map(
        int, input('Введите 3 целых числа через пробел: ').split()
    ))
    print(my_func(a, b, c))
except Exception:
    print('Ошибка ввода!')
