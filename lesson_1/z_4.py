a = input('Введите целое положительное число: ')
i = len(a) - 1
max_a = int(a[i])

while i > 0:
    i -= 1
    if max_a < int(a[i]):
        max_a = int(a[i])

print('самая большая цифра в числе :', max_a)
