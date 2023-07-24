print('++-- \033[1;35;43mTRATAMENTO DE NUMEROS ALEATÓRIOS. \033[m--++')
maior = menor = soma = contador =0
continuar = 's'
while continuar.lower() == 's':
    numero = int(input("Digite um número inteiro: "))
    soma += numero
    contador += 1
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    continuar = input("Deseja continuar? (s/n): ")
media = soma / contador
print('Quantidade de numeros digitados: {}'.format(contador))
print("Média dos valores {}".format(media))
print("Maior valor: {}".format(maior))
print("Menor valor: {}".format(menor))
