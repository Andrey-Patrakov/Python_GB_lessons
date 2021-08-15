class Complex:
    def __init__(self, a, bi):
        self.a = a
        self.bi = bi

    def __add__(self, other):
        if type(other) is Complex:
            return Complex(self.a + other.a, self.bi + other.bi)

        raise TypeError("Неверный тип данных")

    def __mul__(self, other):
        if type(other) is Complex:
            return Complex(
                self.a * other.a - self.bi * other.bi,
                self.bi * other.a + self.a * other.bi
            )

    def __str__(self):
        return f'({self.a}+{self.bi}i)'


comp_1 = Complex(-3, 8)
comp_2 = Complex(4, 4)

print(comp_1 + comp_2)
print(comp_1 * comp_2)
