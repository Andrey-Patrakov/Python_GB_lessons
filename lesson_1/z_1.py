a = input("Введите несколько чисел, разделённых через пробел: ")
a = a.strip().split(" ")
a = list(map(int, a))
a.sort()
print('Отсортирванный список:', *a)

name = input("Как вас зовут?\n")
print(f"Привет {name}!")
