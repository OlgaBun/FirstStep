# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y.
# Задание реализуйте в виде функции my_func(x, y).


def my_pow_fun(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'Error x must be bigger then 0,  y must be less then 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result *= 1 / x
                return f'результат возведения х в степень y: {round(result, 6)}'
    except ValueError:
        return 'Program only works with numbers.'

num1 = input('Enter real positive num, x = ')
num2 = input('Enterь integer negative num, y = ')

print(my_pow_fun(5, -9))