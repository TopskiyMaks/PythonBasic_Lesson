print('Задача 2. Должники')

# Должники и законопослушные граждане хранятся в одной базе банка.
# Из этой базы нам выделяются по 10 человек, у каждого из которых есть свой номер.
# Правда, иногда база глючит и выдаёт нам отрицательный номер.
# А ещё по статистике, которую собрал наш МирПрогБанк,
# каждый второй, кто в этом году брал кредит, не выплатил его вовремя.
#
# Пользователь вводит 10 чисел.
# Напишите программу,
# которая определяет, сколько из них являются одновременно четными и положильными.

nums = []
for _ in range(10):
    num = int(input('Введите числа: '))
    nums.append(num)
n = 0
for num in nums:
    if num % 2 == 0 and num > 0:
        n += 1
print(f'Одновременно четными и положильными являются {n} чисел')
