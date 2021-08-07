from time import time, sleep

class TrafficLight:

    def __init__(self, color):
        self.__color = color
        self.__time = 0
    
    def running(self, color):
        colors = ('red', 'yellow', 'green')
        if self.__color == colors[colors.index(color) - 1]:
            if time() >= self.__time:
                self.__color = color
                self._set__time(color)
                return self.__color
            
            raise Exception('Слишком рано!')
        raise Exception('Неверный порядок переключения цветов')
    
    def _set__time(self, color):
        if color == 'red':
            self.__time = time() + 7
        elif color == 'yellow':
            self.__time = time() + 2
        else:
            self.__time = time() + 5


traffic_light = TrafficLight('red')
try:
    print(traffic_light.running('yellow'))

    sleep(2)
    print(traffic_light.running('green'))

    sleep(5)
    print(traffic_light.running('red'))

    # sleep(6) # Слишком рано!
    sleep(7)
    print(traffic_light.running('yellow'))

    sleep(2)
    # print(traffic_light.running('red')) # Неверный порядок
    print(traffic_light.running('green'))

except Exception as e:
    print(e)
