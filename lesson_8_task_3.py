# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# Поэкспериментируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# Функция в качестве аргумента будет принимать атакующего и атакуемого.
# В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

player_name = input('Введите имя игрока: ')
enemy_name = input('Введите имя врага: ')

player = {'name': player_name, 'health': 100, 'damage': 50, 'armor': 1.2}
enemy = {'name': enemy_name, 'health': 50, 'damage': 30, 'armor': 1}

print('Участники битвы:')
print(player)
print(enemy)


def get_damage(damage, armor):
    return damage/armor


def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage


print('Игрок атакует врага')
attack(player, enemy)
print(enemy)
