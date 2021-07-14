print('Задача 9. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709


def sum_of_range(x, precision):
    previous = 0
    i = 0
    curr = fn = xn = 1
    while abs(curr - previous) > precision:
        previous = curr
        xn *= x * x
        i += 1
        fn *= 2 * i * (2 * i - 1)
        curr += (-1 if i % 2 else 1) * xn / fn
    return curr


if __name__ == '__main__':
    precision = float(input('Введите точность: '))
    x = float(input('Введите x: '))
    print(sum_of_range(x, precision))
