print('Задача 9. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29


n = int(input())
lend = len(str(n * (n + 1) // 2 - 1)) + 2
lens = 2 * n * (lend - 1) - lend
for i in range(n):
    a = (i + 1) * i + 1
    m = range(a, a + 2 * (i + 1), 2)
    tmp = (' ' * lend).join(list(map(str, m)))
    print('{:^{r}}'.format(tmp, r=str(lens)))
