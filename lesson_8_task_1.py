# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»


def write_info(name, age, city):
    string = f'{name}, {age} год(а), проживает в городе {city}'
    return string


my_name = input('Введите имя: ')
my_age = input('Введите возраст: ')
my_city = input('Введите город проживания: ')

print(write_info(my_name, my_age, my_city))
