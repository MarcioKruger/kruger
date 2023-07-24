print('===' * 15)
print('       --- ESTATÍSTICA DO FUTEBOL ---')
print('===' * 15)
lista = [] #Lista para adicionar os dicionários contendo as informações do jogadores cadastrados.
while True:
    jogador = {}  #Dicionário para adicionar as informações de cada jogador.
    nome = str(input('Nome do jogador: '))
    jogador['Jogador'] = nome #adiciona o nome do jogador no dicionário.
    partidas = int(input(f'Quantas partidas {nome} jogou: '))
    jogador['partidas'] = partidas #adiciona a quantidade de partidas no dicionário.
    print('===' * 15)
    quantidade = {}  #Dicionário para adicionar a quantidade de partidas de cada jogador cadastrado.

    #Estrutura para cadastrar os gols de cada partida do jogador.
    for i in range(partidas):
        gol = int(input(f'Quantos gols na Partida {i + 1}: '))
        quantidade[f'Partida {i + 1}'] = gol
    c = 0
    for i, k in quantidade.items():
        c = k + c
    #Duas listas que recebe quantidade de gols e o total de gols de todas as partidas.
    jogador['total'] = c
    jogador['gols'] = quantidade
    lista.append(jogador)
    #Estrutura criar mais uma lista com os dados de mais um jogador a ser cadastrado.
    pergunta = str(input('Adciconar mais um josgador? [S/N]: ')).upper()
    if pergunta == 'N':
        break
#Mostra os jogadores cadastrados com algumas informações sobre os jogadores.
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
#Estrutura que pergunta se o usuário quer ver as estatísticas completas de cada jogador.
while True:
    pergu = str(input('Deseja ver estatísticas: S/N ')).upper().split()[0]
    if pergu == 'S':
        #Estrutura que pergunta o nome do jogador para ser obtido uma análise mais completa.
        p = str(input('Digite o nome do jogador: '))
    else:
        break
    #Código que verifica se o nome do jogador digita pelo usuário está cadastrado.
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
    #Código que mostra as estatísticas do jogador que o usuário digitou para analisar.
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
