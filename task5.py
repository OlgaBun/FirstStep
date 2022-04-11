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
