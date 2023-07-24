import random
import time
n = random.randint(0,5)
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 5, tente advinhar!')
a = int(input('Que numero eu pensei?: '))
print('Processando...')
time.sleep(1)
if a == n:
    print('Você falou {} e eu pensei no {}. parabéns, você acertou!'.format(a, n))
else:
    print('eu pensei {} e você falou {} numero errado!!!'.format(n, a))
print('-=-' * 20)
