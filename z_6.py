import os
print("Cтруктура \"Товары\"")
print("Введите через пробел название, цену, количество и единицы товара")
print("Чтобы закончить ввод данных введите пустую строку")
input("Нажмите Enter чтобы начать заполнять данные...")

i = 1
my_list = []
while True:
    os.system("cls")
    print(*my_list, sep = "\n")
    print("[название] [цена] [количество] [eд]")
    try:
        inp = input()
        if inp.strip() == "": 
            break
        else:
            name, price, count, unit = inp.split()
            my_list += [(i, {"название": name, "цена": float(price), 
                "количество": int(count), "eд": unit}
            )]

    except:
        print("Ошибка ввода данных!")
        input("Нажмите Enter чтобы продолжить...")
        continue

    i += 1

name = set()
price = list()
count = list()
unit = set()

for line in my_list:
    for key, value in line[1].items():
        if key == 'название':
            name.add(value)
        elif key == 'цена':
            price += [value]
        elif key == 'количество':
            count += [value]
        elif key == 'eд':
            unit.add(value)

analytics = {
    'название': list(name),
    'цена': price,
    'количество': count,
    'eд': list(unit)
}

os.system("cls")
print(*my_list, sep = "\n")
print(f"{'='*40}\nПо товарам была собрана аналитика\n{'='*40}")

for key, value in analytics.items():
    print(f'{key}: {value}')
