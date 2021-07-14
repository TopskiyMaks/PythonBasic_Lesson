import random

print('Задача 9. Недоделка')


# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.


def rock_paper_scissors():
    var = ['ножницы', 'камень', 'бумага']
    answer = input('Камень, ножницы или бумага?')
    if answer.lower() == random.choice(var):
        print('Вы победили!')
    else:
        print('Вы проиграли!')
    print()


def guess_the_number():
    guesses_made = 0
    number = random.randint(1, 10)
    while True:
        guess = int(input('Введи число: '))
        guesses_made += 1
        if guess < number:
            print('Твое число меньше.')
        if guess > number:
            print('Твое число больше.')
        if guess == number:
            print(f'Ты угадал! С {guesses_made} попытки')
            break


def mainMenu():
    while True:
        game = int(input('Выберите игру:\n'
                         '1 - Угадай число\n'
                         '2 - Камень, ножницы, бумага\n'
                         '0 -  Выход\n'))
        print()
        if game == 1:
            guess_the_number()
        elif game == 2:
            rock_paper_scissors()
        elif game == 0:
            return
        else:
            print('Неверная команда!')


if __name__ == '__main__':
    mainMenu()