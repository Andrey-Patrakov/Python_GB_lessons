my_list = input("Введите несколько слов через пробел.\n").split()
for i in range(len(my_list)):
    print(f"{i+1}: {my_list[i][:10]}")
