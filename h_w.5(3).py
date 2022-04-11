# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч
# вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as f:
    salary_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(salary_dict.values()) / len(salary_dict), 3)}\n'
          f'Employees with salary less than 20k {[e[0] for e in salary_dict.items() if e[1] < 20000]}')
