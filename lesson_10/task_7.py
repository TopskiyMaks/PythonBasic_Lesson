print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

n = int(input("Сколько будет чисел? "))
max_sum = 0
N = 0
for i in range(n):
    m = int(input("Число " + str(i + 1) + ": "))
    N = m
    sum_nums = 0
    while m != 0:
        num = m % 10
        sum_nums += num
        m = m // 10
    if max_sum < sum_nums:
        max_num = N
        max_sum = sum_nums
print(N, max_sum)
