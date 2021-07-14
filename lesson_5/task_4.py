print('Задача 4. Поступление')

# В университете на особый факультет на направление кибернетики
# очень серьёзный конкурс — поступают только сильнейшие,
# первые десять человек из списка.
# Потом среди поступивших определяется, кто будет на стипендии.
# Для стипендии общий балл при поступлении должен составлять не менее 290.

# Напишите программу,
# которая получает на вход место студента в списке и его балл,
# а затем выводит соответствующие сообщения о поступлении и получении стипендии.

# Пример 1:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 295
# Поздравляем, Вы поступили!
# Бонусом Вам будет начисляться стипендия

# Пример 2:
# Введите место в списке поступающих: 3
# Введите количество баллов за экзамены: 270
# Поздравляем, Вы поступили!
# Но Вам не хватило баллов для стипендии

pos = int(input('Введите место в списке поступающих: '))
points = int(input('Введите количество баллов за экзамены: '))
if pos <= 10:
    print('Поздравляем, Вы поступили!')
    if points >= 290:
        print('Вам хватило баллов для стипендии')
    else:
        print('Но Вам не хватило баллов для стипендии')
else:
    print('К сожалению, вы не поступили')
