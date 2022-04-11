# 2. Представлен список чисел. Необходимо вывести элементы исходного списка
#  значения которых больше предыдущего элемента.


my_list = [15, 17, 20, 21, 23, 35, 40]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)

################################################################################################

a = [int(i) for i in input('Enter numbers').split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        print(a[i])