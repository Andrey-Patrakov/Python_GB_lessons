import traceback


class NotANumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


print("Введите числа через пробел")
print("Для остановки ввода введите \"stop\"")

numbers = []
break_flag = False
while not break_flag:
    my_list = []
    for number in input().split():
        if number == "stop":
            break_flag = True
            break
        else:
            try:
                try:
                    my_list += [float(number)]
                except Exception:
                    raise NotANumberException("Введено не число")
            except Exception as e:
                print(f"Ошибка: {e}\n {traceback.format_exc()}")

    numbers += my_list

print(numbers)
