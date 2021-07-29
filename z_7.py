def fact(n):
    out = 1
    yield 1, 0

    for i in range(1, n + 1):
        out *= i
        yield out, i

try:
    a = int(input("Введите целое число: "))
    for f, i in fact(a):
        print(f'{i}! = {f}')
except:
    print("Неверный ввод данных")

