rus = int(input('Введите кол-во баллов по русскому языку: '))
math = int(input('Введите кол-во баллов по математике: '))
inf = int(input('Введите кол-во баллов по информатике: '))
if rus+math+inf >= 270:
  print('Поздравляю, ты поступил на бюджет!')
else:
  print('К сожалению, ты не прошёл на бюджет.')