# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

uniq_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]