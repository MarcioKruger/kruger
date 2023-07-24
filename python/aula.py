print('===' * 15)
print('       --- ESTATÍSTICA DO FUTEBOL ---')
print('===' * 15)
lista = []
while True:
    jogador = {}
    nome = str(input('Nome do jogador: '))
    jogador['Jogador'] = nome
    partidas = int(input(f'Quantas partidas {nome} jogou: '))
    jogador['partidas'] = partidas
    print('===' * 15)
    quantidade = {}
    for i in range(partidas):
        gol = int(input(f'Quantos gols na Partida {i + 1}: '))
        quantidade[f'Partida {i + 1}'] = gol
    c = 0
    for i, k in quantidade.items():
        c = k + c
    jogador['total'] = c
    jogador['gols'] = quantidade
    lista.append(jogador)
    pergunta = str(input('Adciconar mais um josgador? [S/N]: ')).upper()
    if pergunta == 'N':
        break
print('===' * 15)
print('    Lista de Jogadores: ')
print('--------------------------------')
print('  NOME             | Partidas     | Gols      ')
est = []
for valor in lista:
    pessoas = valor
    print(pessoas["Jogador"], end='                 ')
    print(pessoas["partidas"], end='             ')
    print(pessoas['total'])
    est.append(pessoas)
print()
while True:
    pergu = str(input('Deseja ver estatísticas: S/N ')).upper().split()[0]
    if pergu == 'S':
        p = str(input('Digite o nome do jogador: '))
    else:
        break
    encontrado = None
    for dicionario in est:
        if dicionario['Jogador'] == p:
            encontrado = dicionario
            break
    if encontrado:
        print(f'{encontrado["Jogador"]} encontrado')
    else:
        print(f'{p} não encontrado')
        break
    c = 0
    for i, k in quantidade.items():
        c = k + c
    encontrado['total'] = c
    encontrado['gols'] = quantidade
    print('===' * 15)
    for i, k in encontrado.items():
        print(f'{i} => {k}')
    print('===' * 15)
    tirado = encontrado['gols']
    g = len(tirado)
    print(f'O jogador {encontrado["Jogador"]} jogou {g} partidas:')
    print()
    for i, k  in tirado.items():
        print(f'   => Na partida {i}, fez {k} gols')
    print('===' * 15)
    print(f"     -> Fez um total de {encontrado['total']} Gols...")
    quat = len(encontrado['gols'])
    media = encontrado['total'] / quat
    print(f'     -> Teve uma media de {media:.1f} gols por partida.')
print('===' * 15)
print()
print('    ===== ESTATÍSTICA ENCERRADAS =====')
print()
