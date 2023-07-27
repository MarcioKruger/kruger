print('===' * 15)
print('       --- FICHA DO JOGADOR ---')
print('===' * 15)

def ficha(nome=0, gols=0):
    if nome == 0:
        return '<desconhecido>'
    return '<desconhecido>'

#Programa principal
nome = str(input('Nome do jogador: '))
gol = str(input('Número de Gols: '))
if gol.isnumeric():
    gol = int(gol)     
else:
    gol = 0
ficha(nome, gol)
print(f'O jogador {ficha(nome)} fez {gol} gol(s) no campeonato. ')
print()
