import sys
if 1 < len(sys.argv) < 5:
    try:
        time = int(sys.argv[1])
        rate = float(sys.argv[2])
        prem = float(sys.argv[3])
        print(f'Зароботная плата сотрудника = {time * rate + prem}')
    except:
        print("Указан неверный тип данных")
else:
    print("Указано неверное количество параметров")
    print("Необходимо указать выработку в часах, ставку и премию через пробел")