print('++-- \033[1;35;43mSOMA DOS NUMEROS ALEATÓRIOS. \033[m--++')
cont = 0
n = 0
soma = 0
n = int(input('Numero: '))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Numero: '))
print('A soma do nuemros é {}, foram digitados {} numeros'.format(soma, cont))
