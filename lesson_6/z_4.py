class Car:

    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, direction):
        if direction == 'left':
            return 'Машина повернула налево'
        elif direction == 'right':
            return 'Машина повернула направо'

        return 'Машина продолжает ехать прямо'

    def show_speed(self):
        return str(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Слишком высокая скорость! {self.speed} > 60'

        return self.speed


class SportCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Слишком высокая скорость! {self.speed} > 40'

        return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police: bool):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(80, 'red', 'Lada 21099', False)
sport_car = SportCar(80, 'yellow', 'Dodge Viper', False)
work_car = WorkCar(80, 'black', 'GAZ 3309', False)
police_car = PoliceCar(80, 'white', 'Lada Vesta', True)

print(town_car.speed)
print(town_car.color)
print(town_car.name)
print(town_car.is_police)
print(town_car.stop())
print(town_car.go())
print(town_car.turn('left'))
print(town_car.turn('right'))
print(town_car.turn('up'))
print(town_car.show_speed())
print()

print(sport_car.speed)
print(sport_car.color)
print(sport_car.name)
print(sport_car.is_police)
print(sport_car.stop())
print(sport_car.go())
print(sport_car.turn('left'))
print(sport_car.turn('right'))
print(sport_car.turn('up'))
print(sport_car.show_speed())
print()

print(work_car.speed)
print(work_car.color)
print(work_car.name)
print(work_car.is_police)
print(work_car.stop())
print(work_car.go())
print(work_car.turn('left'))
print(work_car.turn('right'))
print(work_car.turn('up'))
print(work_car.show_speed())
print()

print(police_car.speed)
print(police_car.color)
print(police_car.name)
print(police_car.is_police)
print(police_car.stop())
print(police_car.go())
print(police_car.turn('left'))
print(police_car.turn('right'))
print(police_car.turn('up'))
print(police_car.show_speed())
