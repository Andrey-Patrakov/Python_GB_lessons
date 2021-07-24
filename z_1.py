def division(a, b):
    try:
        a, b = float(a), float(b)
        return(str(a/b))
    except Exception as e:
        if type(e) is ZeroDivisionError:
            return 'Ошибка: деление на 0!'
        elif type(e) is ValueError:
            return "Ошибка: Указано не число"
        else:
            return e

try:
    a, b = input("Введите 2 числа через пробел: ").split()
    print(division(a, b))
except:
    print("Ошибка ввода")
