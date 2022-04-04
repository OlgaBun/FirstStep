my_list2 = list(input('Enter your numbers - '))

for i in range(1, len(my_list2), 2):
    my_list2[i - 1], my_list2[i] = my_list2[i], my_list2[i - 1]

print(my_list2)
