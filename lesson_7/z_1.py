class Matrix:

    def __init__(self, matrix):
        try:
            self.matrix = [
                list(
                    [float(elem) for elem in row]
                ) for row in matrix
            ]
        except Exception:
            raise TypeError("Неверный тип данных")

    def __str__(self):
        s = [
            "|".join(
                [str(elem).center(10) for elem in row]
            ) for row in self.matrix
        ]

        return "|" + "|\n\n|".join(s) + "|"

    def __add__(self, other):
        res = []
        if type(other) is Matrix:
            try:
                for i in range(len(self.matrix)):
                    res.append([a + b for a, b in zip(self.matrix[i],
                                                      other.matrix[i])])
            except Exception:
                pass

            return Matrix(res)

        raise TypeError("Неверный тип данных")


matrix_1 = Matrix([
    [1, 2, 3, 4, 5],
    [2, 4, 5, 6, 7],
    [3, 5, 6, 7, 8],
    [4, 6, 7, 8, 9],
    [5, 7, 8, 9, 10],
])

matrix_2 = Matrix([
    [10, 9, 8, 7],
    [9, 8, 7, 6],
    [8, 7, 6, 5],
    [7, 6, 5, 4]
])

try:
    print(matrix_1 + matrix_2)
except Exception() as e:
    print(e)
