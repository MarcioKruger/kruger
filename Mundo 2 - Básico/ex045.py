import random
from time import sleep
print('-=-' * 30)
print('{:=^100}'.format(' Vamos Jogar PEDRA, PAPEL e TESOURA. '))
print('*' * 35)
itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)
print('Escola sua opção:')
op = int(input('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
            >: '''))
print('*' * 35)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('*' * 35)
print('O Computador escolheu {}'.format(itens[pc]))
print('O Jogador escolher {}'.format(itens[op]))
if pc == 0:
    if op == 0:
        print('EMPATOU')
    elif op == 1:
        print('JOGADOR VENCEU')
    elif op == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1:
    if op == 0:
        print('COMPUTADOR VENCEU')
    elif op == 1:
        print('EMPATOU')
    elif op == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada inválida')
elif pc == 2:
    if op == 0:
        print('JOGADOR VENCEU')
    elif op == 1:
        print('COMPUTADOR VENCEU')
    elif op == 2:
        print('EMPATOU')
    else:
        print('Jogada inválida')
print('*' * 35)
print('-=-' * 30)
