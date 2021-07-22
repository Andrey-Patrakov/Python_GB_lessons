my_list = [7, 5, 3, 3, 2]
print(*my_list)
num = input("Введите целые числа через пробел? чтобы добавить их в рейтинг.\n")
try:
    my_list += list(map(int, num.split()))
    my_list.sort(reverse=True)
    print(*my_list)
except:
    print("Ошибка ввода данных!")