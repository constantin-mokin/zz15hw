from random import randint

x = randint(0, 100)
counter = 0
counter_summ = 0
a = -1

counter = int(input('vvedi kolichestvo popitok --->   '))

while a != x:
    a = int(input('vvedi chislo ot 0 do 100 --->        '))
    counter_summ += 1
    if a == x:
        print('You are the winner')
    if a < x:
        print('davai bolshe')
    if a > x:
        print('davai menshe')
    if counter_summ == counter:
        print('You are the loser')
        break
