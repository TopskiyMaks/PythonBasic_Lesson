print('Задача 9. ...Теперь можно посчитать и свою')

# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
#
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.

prev_num = 0
check = True
MIN = 0
MAX = 0
for _ in range(0, 10):
    num = int(input('Введите число: '))
    if num < prev_num:
        check = False
    prev_num = num
print(check)
