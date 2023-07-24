print('++-- \033[1;35;43mSOMA DE NUMEROS PARES! \033[m--++')
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o numero {}: '.format(c)))
    if num % 2 == 0:
        soma = num + soma
        cont = cont + 1
print('Você informaou {} numeros PARES, e a soma deles é: {}'.format(cont, soma))
