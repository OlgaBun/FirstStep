# Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна; проверить работу метода
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    __length =  None
    __width = None
    weigh = None
    thickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Creat road')

    def intake(self):
        self.weight = 25
        self.thickness = 0.05
        intake = self.length * self.width * self.weigh * self.thickness / 1000
        print(f'Need {intake} ton for building')

road = Road(20000, 6)
road.intake()
