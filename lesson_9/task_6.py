print('Задача 6. Спецшифр')

# Два сотрудника спецслужб переписываются необычным шифром.
# Каждую букву они шифруют в виде строки,
# внутри которой есть длинная последовательность букв “s”, 
# а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.
# 
# Напишите программу,
# которая получает на вход строку,
# подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.
# 
# Пример:
# Введите строку: ssbbbsssbc
# Самая длинная последовательность: 3

string = input('Введите строку: ')
letters = list(string)
sequence = 0
max_sequence = 0
for i in letters:
    if i == 's':
        sequence += 1
        if sequence > max_sequence:
            max_sequence = sequence
    else:
        sequence = 0
print(max_sequence)