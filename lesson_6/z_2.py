class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass_per_meter, thickness):
        return self._length * self._width * mass_per_meter * thickness / 1000


r = Road(20, 5000)
print(f'{r.calc_mass(25, 5)} т')
