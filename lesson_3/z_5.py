def sum_input():
    s = 0
    stop = False
    while not stop:
        line = input().split()
        for elem in line:
            try:
                s += float(elem)

            except Exception:
                if elem == 'stop':
                    stop = True
                    break

    return s


print("Вводите числа через пробел")
print("Запрещённые символы игнорируются")
print('Чтобы остановить программу введите "stop"')
print(f'Сумма введённых чисел: {sum_input()}')
