# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stoped'

    def turn(self, direction):
        return f'{self.name} Car turned to + direction'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class Sportcar:
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class Towncar:
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')
        if self.speed > 40:
         return f'Speed of {self.name} is higher than allowed for town car'
        else:
             return f'Speed of{self.name} is normal foe towncar'


class WorkCar:
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print (f'Current speed {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher then allowed'


class PoliceCar:
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is police department'
        else:
            return f'{self.name} is not police department'



Lexus = Sportcar(200, 'Blue', 'RX-300', False)
skoda = Towncar(100, 'White', 'Skoda', False)
Bmw = WorkCar(150, 'black', 'Bmw', True)
Audi = PoliceCar(100, 'Blue', 'Audi', True)
print(Bmw.name, Bmw.color. Bmw.speed, Bmw.is_police)
print(Bmw.go(), Bmw.turn('City'), Bmw.stop())
print(Lexus.show_speed)
print(skoda.name, skoda.color, skoda.speed, skoda.is_police)
print(skoda.go(), skoda.turn('City'), skoda.stop)
print(Audi.show_speed())