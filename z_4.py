from z_4_storage import Storage, Equipment


class Printer(Equipment):
    scan = True
    print_speed = 10
    color_print = True
    print_type = ""


class Scanner(Equipment):
    scanner_type = ""


class Xerox(Equipment):
    print_type = ""
    print_speed = 10
    color_print = False


printer_1 = Printer(
    "Canon printer 1", 3, color_print=True, print_type="Струйный",
    dpi="600X1200", scan=False, print_speed=5
)
printer_2 = Printer(
    "Canon printer 1", 7, color_print=True, print_type="Струйный",
    dpi="600X1200", scan=False, print_speed=5
)
printer_3 = Printer(
    "Canon printer 2", 2, color_print=False, print_type="Лазерный",
    dpi="600X1200", scan=False, print_speed=20
)
printer_4 = Printer(
    "Epson printer 1", 4, color_print=True, print_type="Струйный",
    dpi="4800X1200", scan=False, print_speed=10
)
printer_5 = Printer(
    "Samsung printer 1", 5, color_print=True, print_type="Струйный",
    dpi="4800X1200", scan=False, print_speed=7
)

scanner_1 = Scanner("Espada scanner 1", 5, scanner_type="Ручной")
scanner_2 = Scanner("Espada scanner 2", 3, scanner_type="Слайд")
scanner_3 = Scanner("Espada scanner 3", 5, scanner_type="Планшетный")
scanner_4 = Scanner("Epson scanner 1", 7, scanner_type="Слайд")
scanner_5 = Scanner("Epson scanner 2", 1, scanner_type="Ручной")

xerox_1 = Xerox(
    "Epson xerox 1", 2,
    print_type="Струйный", print_speed=7, color_print=True
)
xerox_2 = Xerox(
    "Epson xerox 2", 1,
    print_type="Струйный", print_speed=12, color_print=True
)
xerox_3 = Xerox(
    "Xerox xerox 1", 1,
    print_type="Струйный", print_speed=9, color_print=True
)
xerox_4 = Xerox(
    "Xerox xerox 2", 3,
    print_type="Лазерный", print_speed=20, color_print=False
)
xerox_5 = Xerox(
    "Samsung xerox 1", 2,
    print_type="Струйный", print_speed=11, color_print=True
)

storage = Storage()

storage.put_on_rack("Стеллаж 1", printer_1)
print(storage)  # Кол-во 3

storage.put_on_rack("Стеллаж 1", printer_2)  # Одинаковый с первым, только 7 шт
# storage.put_on_rack("Стеллаж 2", printer_3)
# storage.put_on_rack("Стеллаж 2", printer_4)
# storage.put_on_rack("Стеллаж 2", printer_5)

# storage.put_on_rack("Стеллаж 1", scanner_1)
# storage.put_on_rack("Стеллаж 2", scanner_2)
# storage.put_on_rack("Стеллаж 2", scanner_3)
# storage.put_on_rack("Стеллаж 3", scanner_4)
# storage.put_on_rack("Стеллаж 3", scanner_5)

# storage.put_on_rack("Стеллаж 3", xerox_1)
# storage.put_on_rack("Стеллаж 3", xerox_2)
# storage.put_on_rack("Стеллаж 1", xerox_3)
# storage.put_on_rack("Стеллаж 2", xerox_4)
# storage.put_on_rack("Стеллаж 1", xerox_5)

print(storage)  # Склад - 10, Подразделение 0

storage.send_in_unit("Подразделение 1", "Стеллаж 1", "Canon printer 1", 3)
print(storage)  # Склад - 7, Подразделение 3

try:  # Отдать в подразделение больше, чем есть на складе
    storage.send_in_unit("Подразделение 2", "Стеллаж 1", "Canon printer 1", 10)
except Exception as e:
    print(e)

storage.send_in_unit("Подразделение 2", "Стеллаж 1", "Canon printer 1", 7)
print(storage)  # Запись удалена со склада тк кол-во 0

try:
    storage.send_in_unit("Подр 1", "Стеллаж 1", "Canon printer 1", 1)
except Exception as e:
    print(e)  # Отсутствует на складе
