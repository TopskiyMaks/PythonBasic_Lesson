print('Задача 10.')

# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
#
# Вводится число N,
# далее еще N − 1 чисел:
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.\

N = int(input('Введите число: '))
full_nums = []
nums = [N]
for i in range(1, N + 1):
    full_nums.append(i)
print(full_nums)
for _ in range(N - 2):
    num = int(input('Введите число: '))
    nums.append(num)
print(nums)
for n in full_nums:
    if not n in nums:
        print(n)
