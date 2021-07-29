import itertools

try:
    a = int(input("Введите целое число: "))
except:
    print("Неверный ввод данных")

i = 0
for i in itertools.count(a):
    print(i)
    if i >= a + 10:
        break
    i += 1


my_string = input("Введите строку символов, которые нужно повторять: ")

i = 0
for ch in itertools.cycle(my_string):
    print(ch)
    if i > 30:
        break
    i += 1

