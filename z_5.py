class Stationery:
    
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки 1 ({self.title})")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки 2 ({self.title})")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки 3 ({self.title})")

stationery = Stationery("123")
stationery.draw()

pen = Pen("ручка")
pen.draw()

pencil = Pencil("карандаш")
pencil.draw()

handle = Handle("маркер")
handle.draw()

