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