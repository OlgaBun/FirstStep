#  Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translate_dict = {'One:' 'Один', 'Two:' 'Два', 'Three:' 'Три', 'Four:' 'Четыре'}

with open('text_33.txt', 'w', encoding='utf-8') as new_file:
    with open('text_3.txt', encoding='utf-8') as my_file:
         new_file.writelines([line.replace(line.split()[0], translate_dict.get(line.split()[0])) for line in my_file])
