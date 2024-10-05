from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def textile(self):
        pass


class Coat(Clothes):

    def __init__(self, name, V):
        self.V = V
        super().__init__(name)

    @property
    def textile(self):
        return self.V / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, H):
        self.H = H
        super().__init__(name)

    @property
    def textile(self):
        return 2 * self.H + 0.3


coat = Coat("Пальто", 126)
print(f"Расход ткани на '{coat.name}': {coat.textile}")

suit = Suit("Костюм", 180)
print(f"Расход ткани на '{suit.name}': {suit.textile}")

print(f"Общий расход ткани: {suit.textile + coat.textile}")
