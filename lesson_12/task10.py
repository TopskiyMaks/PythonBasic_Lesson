print('Задача 10')


# Напишите игру - текстовый квест.
# Игрок находится в квартире, его задача - покинуть ее.
# 
# Игрок свободно перемещается по квартире, пока не покинет ее.
# 
# В квартире есть три комнаты (спальня, кухня, ванна) и коридор.
# В ванну можно попасть из коридора и спальни.
# В спальню можно попасть из ванны и коридора.
# На кухню можно попасть только из коридора.
# Коридор связан со всеми комнатами, но в нем дополнительно есть дверь наружу.
# На кухне открыто окно.
# Если игрок пытается выбраться через него, то разбивается и проигрывает


# Пример:

# Вы в спальне. Куда идем?
# 1 - в ванну
# 2 - в коридор

# 2

# Вы в коридоре. Куда идем?
# 1 - в спальню
# 2 - в ванну
# 3 - на кухню
# 4 - в дверь

# 2

# Вы в ванне. Куда идем?
# 1 - в коридор
# 2 - в спальню

# 2

# Вы в спальне...

def game_of_house():
    bedroom()


def hall():
    print('Вы в коридоре. Куда идем?')
    room = int(input(('1 - в спальню\n'
                      '2 - в ванну\n'
                      '3 - на кухню\n'
                      '4 - в дверь\n')))
    if room == 1:
        return bedroom()
    elif room == 2:
        return bathroom()
    elif room == 3:
        return kitchen()
    elif room == 4:
        return door()


def bedroom():
    print('Вы в спальне. Куда идем?')
    room = int(input(('1 - в ванну\n'
                      '2 - в коридор\n')))
    if room == 1:
        return bathroom()
    elif room == 2:
        return hall()


def bathroom():
    print('Вы в ванной. Куда идем?')
    room = int(input(('1 - в коридор\n'
                      '2 - в спальню\n')))
    if room == 1:
        return hall()
    elif room == 2:
        return bedroom()


def kitchen():
    print('Вы на кухне. Куда идем?')
    room = int(input(('1 - в коридор\n'
                      '2 - в окно\n')))
    if room == 1:
        return hall()
    elif room == 2:
        return window()


def window():
    print('Вы вышли в окно и разбились. Вы проиграли!')


def door():
    print('Вы покинули квартиру, Поздравляю!')


if __name__ == '__main__':
    game_of_house()