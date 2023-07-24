print('++-- \033[1;36;42mVerificação de maioriade. \033[m--++')
import datetime
cont = 0
contm = 0
for c in range(1, 8):
    ano = int(input('Digite o {}º ano: '.format(c)))
    maioridade = (datetime.datetime.now().year) - ano
    if maioridade >= 21:
        contm  = contm + 1
    else:
        cont = cont + 1
print('De {} pessoas, {} ainda são menores de idade e {} ja são maiores de idade.'.format(c, cont, contm))
