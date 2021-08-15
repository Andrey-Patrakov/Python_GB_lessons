class Equipment:
    model = ""
    count = 0
    dpi = ""

    def __init__(self, model, count, **args):
        if count < 0:
            raise ValueError("Кол-во единиц не может быть меньше 0")

        self.model = model
        self.count = int(count)

        if "dpi" in args:
            self.dpi = args["dpi"]
        if "scan" in args:
            self.scan = bool(args["scan"])
        if "print_speed" in args:
            self.print_speed = int(args["print_speed"])
        if "color_print" in args:
            self.color_print = bool(args["color_print"])
        if "print_type" in args:
            self.print_type = args["print_type"]
        if "scanner_type" in args:
            self.scanner_type = args["scanner_type"]

    def __add__(self, other):
        if self.model == other.model and type(self) == type(other):
            return type(self)(
                self.model, self.count + other.count, **self.get_args()
            )
        raise TypeError("Неверный тип данных")

    def __sub__(self, other):
        if self.model == other.model and type(self) == type(other):
            return type(self)(
                self.model, self.count - other.count, **self.get_args()
            )
        raise TypeError("Неверный тип данных")

    def __str__(self):
        s = ""
        s = f'Устройство класса {type(self).__name__}:\n'
        s += f'• Модель: {self.model}\n'
        s += f'• Количество: {self.count}\n'

        args = self.get_args()

        if "dpi" in args:
            s += f'• Разрешение: {self.dpi}\n'
        if "print_type" in args:
            s += f'• Тип принтера: {self.print_type}\n'
        if "scanner_type" in args:
            s += f'• Тип сканера: {self.scanner_type}\n'
        if "scan" in args:
            s += f'• Наличие сканера: {"Есть" if self.scan else "Нет"}\n'
        if "print_speed" in args:
            s += f'• Скорость печати: {self.print_speed}\n'
        if "color_print" in args:
            s += f'• Цветная печать: {"Есть" if self.color_print else "Нет"}\n'
        return s + "\n"

    def get_args(self):

        params = {}

        try:
            params["dpi"] = self.dpi
        except Exception:
            pass
        try:
            params["print_type"] = self.print_type
        except Exception:
            pass
        try:
            params["scanner_type"] = self.scanner_type
        except Exception:
            pass
        try:
            params["scan"] = self.scan
        except Exception:
            pass
        try:
            params["print_speed"] = self.print_speed
        except Exception:
            pass
        try:
            params["color_print"] = self.color_print
        except Exception:
            pass

        return params


class Storage:
    racks = {}  # Стеллаж
    unit = {}  # подразделения компании

    def __str__(self):
        s = f"{'='*30}\n"
        s += "Склад:\n"
        s += f"{'='*30}\n"

        for key, value in self.racks.items():
            s += f"Стеллаж № {key}:\n"
            s += f"{'-'*30}\n"
            for i in value:
                s += str(i)
            s += f"{'-'*30}\n"

        s += f"{'='*30}\n"
        s += "Подразделения:\n"
        s += f"{'='*30}\n"

        for key, value in self.unit.items():
            s += f"Подразделение № {key}:\n"
            s += f"{'-'*30}\n"
            for i in value:
                s += str(i)
            s += f"{'-'*30}\n"

        return s + f"{'='*30}\n"

    def __put_in_dict(self, dict, key, value):
        for base in type(value).__bases__:
            if base is Equipment:

                if key in dict:
                    for eq in range(len(dict[key])):
                        if dict[key][eq].model == value.model:
                            dict[key][eq] += value
                            return

                    dict[key] += [value]
                    return
                else:
                    dict[key] = [value]
                    return
        TypeError("Неверный тип данных")

    def put_on_rack(self, rack, equipment):
        self.__put_in_dict(self.racks, rack, equipment)

    def send_in_unit(self, unit, rack, model, count):
        if rack in self.racks:
            for eq in range(len(self.racks[rack])):
                if self.racks[rack][eq].model == model:
                    eq2 = type(self.racks[rack][eq])(model, count)

                    self.racks[rack][eq] -= eq2
                    self.__put_in_dict(self.unit, unit, eq2)

                    if self.racks[rack][eq].count == 0:
                        del self.racks[rack][eq]

                    return

            raise ValueError("Эта техника отсутствует на складе")

        raise ValueError("Такого стеллажа нет")
