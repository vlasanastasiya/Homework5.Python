# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет

from random import *


start_text = ('Игра началась')
print(start_text)


def game():
    candy = 150

    moves = 28
    count = 0
    player_1 = input('\nПервого игрока зовут: ')
    player_2 = input('\nВторого игрока зовут: ')

   
    x = randint(1, 2)
    if x == 1:
        first = player_1
        second = player_2
    else:
        first = player_2
        second = player_1
    print(f'{first} твой ход первый')

    while candy > 0:
        if count == 0:
         step = int(input(f'\n {first} '))
         if step > candy or step > moves:
            int(input(
                    f'\nможно взять только {moves} конфет, попробуй еще раз: '))
            candy = candy - step
        if candy > 0:
            print(f'\nосталось {candy} конфет')
            count = 1
        else:
            print('Конфет больше нет')

        if count == 1:
            step = int(input(f'\n {second} '))
            if step > candy or step > moves:
               step = int(input(
                    f'\n можно взять только {moves} конфет, попробуй еще раз: '))
            candy = candy - step
        if candy > 0:
            print(f'\nосталось {candy} конфет')
            count = 0
        else:
            print('Конфет больше нет')

    if count == 1:
        print(f'Победил {second}')
    if count == 0:
        print(f'Победил {first}')

game()
