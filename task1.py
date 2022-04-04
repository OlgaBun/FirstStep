my_list = [32, 143.5, None, -128, 'born', True, {7: 'seven', 9: 'nine'},
        [4, 5], (2, 5, 7)]

    for i, item in enumerate(my_list, 1):
        print(f'{i} {item} - {type(item)}')