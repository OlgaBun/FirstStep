# 1.Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def pos_arg(v_1, v_2):
    try:
        v_1, v_2 = int(v_1), int(v_2)
        div = v_1 , v_2
    except ValueError:
        return 'Value Error'
    except ZeroDivisionError:
        return 'Zero Division Error'
    return round(div, 4)

print(pos_arg(input('Enter first num - '), input('Enter second num - ')))



