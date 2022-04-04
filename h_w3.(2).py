# 2. Выполнить функцию, которая принимает несколько параметров,
#    описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
#    email, телефон.
#   Функция должна принимать параметры как именованные аргументы.
#   Осуществить вывод данных о пользователе одной строкой.

def pers_inf(**kwargs):
    return ' '.join(kwargs.values())

name = input('Enter Your name - ')
last_name = input('Enter Your last name  - ')
birthday = input('Enter Your birthday - ')
city = input('Enter Your city - ')
email = input('Enter Your email - ')
phone_num = input('Enter phone number - ')

print(pers_inf(name=name, last_name=last_name, birthday=birthday, city=city, email=email,
               phone_num=phone_num))