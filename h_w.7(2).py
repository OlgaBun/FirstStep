# Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда,
# которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC,abstractmethod

class Clothes(ABC):
    def __init__(self):
        pass
    @property
    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return self.calc + other.calc

    class Coat(Clothes):
        def __init__(self, size):
            super().__init__()
            self.size = size

        @property
        def size(self):
            return.__size

        @size.setter
        def size(self, size):
            if size < 40:
                print('Please, choose your model')
                self.__size = 40
            elif size > 56:
                print('Ok, let`s start')
                self.__size = 56
            else:
                self.__size = size

        @property
        def calc(self):
            return self.__size / 6.5 + 0.5

        class Suit(Clothes):
            def __init__(self, height):
                super().__init__()
                self.height = height

            @property
            def height(self):
                return self.__height

            @height.setter
            def height(self,height):
                if height < 100:
                    print('We don`t sew little models')
                    self.__height = 120
                elif height > 180:
                    print('Let`s start')
                    self.__height = 180
                else:
                    self.__height = height

            @property
            def calc(self):
                return 2 * (self.__height / 100) + 0.3


coat_1 = Coat(int(input('Enter coat`s size:')))
print(f'You`ll need {coat_1.calc:.2f} m for Coat {coat_1.size} size')
suit_1 = Suit(int(input('Enter Your height for calc(please, enter cm):')))
print(f'You`ll need {suit_1.calc:.2f} m for suit {suit_1.height}')
print(f'Total m {coat_1 + costume_1:.2f} m')


