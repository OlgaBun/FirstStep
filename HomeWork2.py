
my_list = [32, 143.5, None, -128, 'born', True, {7: 'seven', 9: 'nine'},
        [4, 5], (2, 5, 7)]

    for i, item in enumerate(my_list, 1):
        print(f'{i} {item} - {type(item)}')
###################################1#########################################
my_list2 = list(input('Enter your numbers - '))

for i in range(1, len(my_list2), 2):
    my_list2[i - 1], my_list2[i] = my_list2[i], my_list2[i - 1]

print(my_list2)

####################################2########################################

month = int(input('Please, enter month'))

seasons = {'Winter': (1, 2, 12),
           'Sping': (3, 4, 5),
           'Summer': (6, 7, 8),
           'Autumn': (9, 10, 11)}

for key in seasons.keys():
    if month in seasons[key]:
        print(key)


#2
month = int(input('Please enter month'))

season_list = ['winter', 'spring', 'summer', 'autumn']
    if month == 1 or month == 12 or month == 2:
        print(season_list[0])
    elif month == 3  or month == 4 or month == 5:
        print(season_list[1])
    elif month == 6 or month == 7 or month ==8:
        print(season_list[2])
    elif month == 9 or month == 10 or month ==11:
        print(season_list[3])
    else: print('month does not exist')

################################3#############################

my_string = input('Enter some words - ').split()
for i, word in enumerate(my_string, 1):
    print(f'{i}, {word[:10]}')

#################################4#############################

my_list = [9, 8, 7, 3, 1, 1]
new_number = int(input('Enter new number - '))
x = 0

for n in my_list:
    if new_number <= n:
        x += 1

    elif new_number > n:
        break

my_list.insert(x, float(new_number))
print(my_list)

