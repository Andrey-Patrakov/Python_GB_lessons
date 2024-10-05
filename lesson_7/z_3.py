class Cell:

    def __init__(self, count: int):
        if type(count) is int:
            if count > 0:
                self.__count = count
                return

            raise ValueError("Количество клеток должно быть больше 0")

        raise TypeError("Неверный тип данных")

    def __add__(self, other):
        if type(other) is Cell:
            return Cell(self.__count + other.__count)

        raise TypeError("Неверный тип данных")

    def __sub__(self, other):
        if type(other) is Cell:
            return Cell(self.__count - other.__count)

        raise TypeError("Неверный тип данных")

    def __mul__(self, other):
        if type(other) is Cell:
            return Cell(self.__count * other.__count)

        raise TypeError("Неверный тип данных")

    def __truediv__(self, other):
        if type(other) is Cell:
            res = round(self.__count / other.__count)
            return Cell(res)

        raise TypeError("Неверный тип данных")

    def __str__(self):
        return str(self.__count)

    @staticmethod
    def make_order(cell, cells_per_row):
        if type(cell) is Cell and type(cells_per_row) is int:

            res = "\n".join([
                "*" * cells_per_row for i in range(cell.__count // cells_per_row) # noqa
            ])
            return f'{res}\n{"*" * (cell.__count % cells_per_row)}'

        raise TypeError("Неверный тип данных")


try:
    cell_0 = Cell(0)  # Количество клеток должно быть больше 0
except Exception as e:
    print(e)

cell_1 = Cell(5)
cell_2 = Cell(24)
cell_3 = cell_1 + cell_2

print(f'Сложение: {cell_3}')

try:
    print(f'Вычитание: {cell_1 - cell_2}')  # Количество клеток должно быть больше 0 # noqa
except Exception as e:
    print(e)

print(f'Вычитание: {cell_2 - cell_1}')
print(f'Умножение: {cell_1 * cell_2}')

try:
    print(f'Умножение: {cell_1 * 2}')  # Неверный тип данных
except Exception as e:
    print(e)

print(f'Деление: {cell_2 / cell_1}')
print(Cell.make_order(cell_3, 8))
