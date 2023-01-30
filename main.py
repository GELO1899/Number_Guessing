from random import *

num = randint(1, 100)
print('Добро пожаловать в числовую угадайку')


def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


def start_game():
    counter = 0
    while True:
        n = input('Введите число от 1 до 100 ')
        counter += 1
        if is_valid(n):
            n = int(n)
            if n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                continue
            elif n > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                continue
            elif n == num:
                print('Вы угадали, поздравляем!')
                print('Кол-во попыток:', counter)
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue


start_game()
while True:
    start = input('Хотите сыграть ещё раз? Да/Нет ')
    if start.lower() == 'да':
        start_game()
    elif start.lower() == 'нет':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
    else:
        print('ERORR')
        continue
