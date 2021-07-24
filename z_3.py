def my_func(a, b, c):
    l = sorted([a, b, c], reverse = True)
    return sum(l[:2:])

try:
    a, b, c = list(map(int, input('Введите 3 целых числа через пробел: ').split()))
    print(my_func(a, b, c))
except:
    print('Ошибка ввода!')