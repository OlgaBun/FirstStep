# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
f = open('text_1.txt', 'w', encoding= 'utf-8')

line = ''
while line:
    line = input('What`s the plan?: ')
    f.write(f'{line}\n') if line != '' else f.close()

