print('++-- \033[1;35;43mCLASSIFICAÇÃO DO CAMPEONATO BRASILEIRO DE FUTEBOL. \033[m--++')
times = ('Botafogo', 'Flamengo', 'Grêmio', 'São Paulo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Athletico-PR', 'Fortaleza',
         'Cruzeiro', 'Internacional', 'Atlético-MG', 'Cuiabá', 'Santos', 'Corinthians', 'Bahia', 'Goiás', 'Coritiba',
         'Vasco da Gama', 'América-MG')
time = 'Grêmio'
print('-=' * 30)
print(f'Os 5 primeros colocados são: {times[:5]}')
print('-=' * 30)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 30)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-=' * 30)
print(f'O {time} está na {times.index(time) + 1}ª Colocação')
print('-=' * 30)
print('FIM DO PROGRAMA')
