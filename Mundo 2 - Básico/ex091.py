import random
import time
print('-=-' * 15)
print('           ++-- \033[1;35;43mJOGANDO DADOS. \033[m--++')
print('-=-' * 15)
jogadores = {}
time.sleep(2)
print()
print(' ------- Jogadores jogam os dados -------')
print()
time.sleep(2)
for i in range(1, 5):
    resultado =  random.randrange(1, 7)
    print(f'Jogador {i}: {resultado}')
    jogadores[f'Jogador {i}'] = resultado
    time.sleep(1)
print('-=-' * 15)
time.sleep(1)
print('++++++ RESULTADO ++++++')
print('-=-' * 15)
time.sleep(2)
jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)
time.sleep(1)
i = 0
for k, v in jogadores_ordenados:
    print(f'{i + 1}º lugar: {k} = {v}')
    i += 1
    primeiro = next(iter(jogadores_ordenados))
print('-=-' * 15)
time.sleep(2)
print(f'O VENCEDOR foi: {primeiro[0]}')
print()
