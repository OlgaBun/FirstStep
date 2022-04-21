# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def change_type(cls, data):
        return f'Day {int(data[0]) :02d}, Month int(data[1]) in range (1, 13) or int(data[2])'

    @staticmethod
    def validation(data):
        if not int(data[0]) in range(1, 32) or not int(data[1]) in range(1, 13) or int(data[2]) > 2020:
            return 'Invalid date!'

    def data_func(self):
        res_1 = Data.change_type(self.data.split('-'))
        res_2 = Data.validation(self.data.split('-'))
        return res_2 if res_2 else f'Refformated data (type int) \n{res_1}'

user_data = input('Enter date (dd-mm-yyyy): ')
mc = Data(user_data)
print(mc.data_func())
user_data = input('Enter date (dd-mm-yyyy): ')
mc_2 = Data(user_data)
print(mc_2.data_func())
print(mc.data_func())