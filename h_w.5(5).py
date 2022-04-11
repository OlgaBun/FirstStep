# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

from random import rendint

with open('text_5.txt', mode='w+', encoding= 'utf-8') as the_file:
    the_file.write(''.join([str(randint(1, 1000)) for _ in(100000)]))
    the_file.seek(0)
    print(sum(map(int, the_file.readline().split())))