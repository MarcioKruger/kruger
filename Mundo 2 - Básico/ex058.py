import random
import time
cont = 1
pc = random.randint(0,10)
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 10, tente advinhar!')
time.sleep(3)
r = int(input('Que numero eu pensei?: '))
print('Processando...')
time.sleep(1)
while r != pc:
    if r > pc:
        print('MENOS... Você falou {} ERRADO!. tentativa {}.'.format(r, cont))
        time.sleep(1)
        r = int(input('Que numero eu pensei: '))
        cont = cont + 1
        time.sleep(1)
    else:
        print('MAIS... Você falou {} ERRADO!. tentativa {}.'.format(r, cont))
        time.sleep(1)
        r = int(input('Que numero eu pensei: '))
        cont = cont + 1
        time.sleep(1)
print('eu pensei {} e você falou {} com {} tentativas! PARABÉNS!!!'.format(pc, r, cont))
print('-=-' * 20)
