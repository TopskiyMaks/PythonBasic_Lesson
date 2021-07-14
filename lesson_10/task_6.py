print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 

N = int(input('Введите число: '))
sum_factorials = 0
for i in range(1, N+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    sum_factorials += factorial
print(sum_factorials)
