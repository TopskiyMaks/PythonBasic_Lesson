print('Задача 4. Отрезок')

#Напишите программу, 
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
N = 0
count = 0
avg = 0
for i in range(a+1, b):
    if i % c == 0:
        print(i)
        N += i
        count += 1
avg = N / count
print(avg)
