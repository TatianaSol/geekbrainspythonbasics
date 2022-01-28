#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.


def max_number(number1, number2, number3):
    max_num = max(number1, number2, number3)
    return max_num


n1 = int(input('Введите 1ое число: '))
n2 = int(input('Введите 2ое число: '))
n3 = int(input('Введите 3ое число: '))

print(f'Максимальное число: {max_number(n1, n2, n3)}')
