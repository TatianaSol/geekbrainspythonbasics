import random

print('Згадайте число от 1 до 100, компьютер попробует его отгадать')

min_number = 1
max_number = 100
user_answer = None

while user_answer != 'равно':
    guess = random.randint(min_number, max_number)
    user_answer = str(input(f'Пробую угадать: {guess}, '
                            f'ответь если введенное число больше, меньше или равно загаданному: '))
    if user_answer == 'больше':
        max_number = guess - 1
    elif user_answer == 'меньше':
        min_number = guess + 1
    else:
        print('Победа!')
