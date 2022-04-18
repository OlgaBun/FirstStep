# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

with open('text_1.txt', 'r', encoding= 'utf-8') as f_obj:
    useful = [f'{line}. {count.strip()} - {len(count.split())} words'
              for line, count in enumerate(f_obj, 1)]
    print(*useful, f'Total string - {len(useful)}.', sep='\n')

