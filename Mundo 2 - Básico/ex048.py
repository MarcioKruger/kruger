print('++-- \033[1;35;43mNÚMEROS DIVISÍVEIS POR 3 \033[m--++')
soma = 0
cont = 0
i = int(input('Digite o valor inicial do range: '))
f = int(input('Digite o valor final do range: '))
for c in range(i, f, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma dos {} numeros divisíveis por 3 no intervalo entre {} e {} é: {}'.format(cont, i, f, soma))
