# Задача №2 (угадайка)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNT_TRY = 10
RAND_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)

class Number:

    def __init__(self,num: int):
        self.num = num

    def suspect_number(self):
        for _ in range(COUNT_TRY + 1):
            if self.num > RAND_NUMBER:
                print('Ваше число БОЛЬШЕ загаданного')
            elif self.num < RAND_NUMBER:
                print('Ваше число МЕНЬШЕ загаданного')
            else:
                print('Вы выиграли!')

num_suspect = Number(10)
print(num_suspect, num_suspect.suspect_number())
