print('Задача 8. Пирамидка')

# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

#
###
#####
#######

x = int(input('Высота пирамиды: '))
for i in range(x):
    print('%s%s' % (' ' * (x - i - 1), '#' * (i * 2 + 1)))