print('Задача 3. Слишком большие числа')

# У неудачливого бухгалтера всё опять идёт наперекосяк:
# ему приносят такие большие счета, что числа не помещаются на бумаге.

# Напишите программу,
# которая считала бы для него,
# сколько десятичных цифр (знаков) во вводимом числе.

num = int(input('Введите число: '))
n = 0
while num > 0:
    num = num // 10
    n += 1
print(n)