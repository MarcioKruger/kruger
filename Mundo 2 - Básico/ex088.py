import random
import time
print('-=-' * 15)
print('++-- \033[1;35;43mPALPITES PARA A MEGA SENA. \033[m--++')
print('-=-' * 15)
perg = int(input('Quantos jogos gostaria de gerar: '))
time.sleep(1)
for c in range(perg):
    jogo = random.sample(range(1, 61), 6)
    jogo.sort()
    print(f'Jogo {c + 1}: {jogo}')
    time.sleep(1)
print('-=-' * 15)
print()
