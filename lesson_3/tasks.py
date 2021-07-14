# Task-1
a = 8
b = 10
c = 12
d = 18
res = ((-3+a**2)*b-2**3)/(c-2*d)
print(res)

# Task-2
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
a *= 3
b %= 8
print(a + b)

# Task-3
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвертое число: '))
sum_1 = a + b
sum_2 = c + d
print(sum_1/sum_2)

# Task-4
a = int(input('Введите число: '))
print(f'После числа {a} идет число {a+1}')
print(f'Перед числом {a} идет число {a-1}')

# Task-5
print('Решите данный пример: 50 * 2^3 − 32')
answer = input('Введите ответ: ')
true_answer = 50 * 2**3 - 32
print('Правильный ответ: ', true_answer)
print('Ваш ответ: ', answer)

# Task-6
a = int(input('Введите первый катет: '))
b = int(input('Введите второй катет: '))
print(f'Площадь треугольника равна {(a+b)/2}')

# Task-7
a = int(input('Введите количество минут: '))
print(f'{a//60} часа {a%60} минут')

# Task-8
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(f'Сумма: {a % 100 + b % 100}')

# Task-9
v = int(input('Введите скорость: '))
t = int(input('Введите количество часов: '))
print((v * t) % 115)

# Task-10
a = int(input('Введите кол-во рублей: '))
b = int(input('Введите кол-во копеек: '))
n = int(input('Введите кол-во пирожков: '))
print(f'Стоимость: {a*n + b*n//100} рублей {b*n%100} копеек')

# Task-11
a = int(input('Введите число: '))
one = a // 1000
two = a // 100
three = a // 10
four = a % 10
print(one)
print(two % 10)
print(three % 10)
print(four)

# Task-12
a = int(input('Введите число: '))
one = a // 1000
two = a // 100
three = a // 10
four = a % 10
print(f'{four * 1000 + three % 10 * 100 + two % 10 * 10 + one}')

# Task-13
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)

a += b
b = a - b
a -= b

print(a, b)
