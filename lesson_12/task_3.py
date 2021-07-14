print('Задача 3. Апгрейд калькулятора')


# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
# 
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
# 
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
# 
# Напишите программу,
# которая спрашивает у пользователя число и действие, 
# которое нужно с ним сделать: 
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру. 
# 
# Каждое действие оформите в виде отдельной функции, 
# а основную программу зациклите.

def calc():
    while True:
        number = int(input('Введите число(0 - выход): '))
        if number == 0:
            break
        operation = int(input('Выберите действие:\n'
                              '1 - Вывести сумму цифр\n'
                              '2 - Вывести максимальную цифру\n'
                              '3 - Вывести минимальную цифру\n'))

        if operation == 1:
            sum_nums(number)
        if operation == 2:
            max_num(number)
        if operation == 3:
            min_num(number)


def sum_nums(number):
    suma = 0
    while number > 0:
        digit = number % 10
        suma = suma + digit
        number = number // 10
    print("Сумма:", suma)


def max_num(number):
    nums = map(int, str(number))
    print(max(nums))


def min_num(number):
    nums = map(int, str(number))
    print(min(nums))


if __name__ == '__main__':
    calc()
