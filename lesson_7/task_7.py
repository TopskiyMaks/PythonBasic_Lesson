print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
nums = []
for i in range(a, b+1):
    if i % 3 == 0:
        nums.append(i)
print(f'Среднее арифметическое всех чисел из отрезка [{a}; {b}], которые кратны числу 3: {int(sum(nums)/len(nums))}')