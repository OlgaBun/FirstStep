my_string = input('Enter some words - ').split()
for i, word in enumerate(my_string, 1):
    print(f'{i}, {word[:10]}')
