jogador = {}
nome = str(input('Nome do jogador: '))
jogador['Jogador'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou: '))
print('===' * 10)
quantidade = {}
for i in range(partidas):
    gol = int(input(f'Quantos gols na Partidas {i + 1}: '))
    quantidade[f'Partida {i + 1}'] = gol
c = 0
for i, k in quantidade.items():
    c = k + c
jogador['total'] = c
jogador['gols'] = quantidade
print('===' * 10)
for i, k in jogador.items():
    print(f'O campo {i} tem o valor {k}')
print('===' * 10)
tirado = jogador['gols']
g = len(tirado)
print(f'O jogador {jogador["Jogador"]} jogou {g} partidas:')
for i, k  in tirado.items():
    print(f'   => Na partida {i}, fez {k} gols')
print(f"Fez um total de {jogador['total']} Gols...")
print()
