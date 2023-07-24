print('++-- \033[1;35;43mCADASTRO DE NÚMEROS SEM REPETIÇÃO. \033[m--++')
lista = []
while True:
    n = int(input('Digite um numero: '))
    if n not in lista:
        lista.append(n)
        print('Adicionado com sucesso!!!')
    else:
        print('Valor Duplicado. Não será adicionado.')
    resposta = input("Deseja continuar? (s/n): ").upper().split()[0]
    if resposta in 'N':
        break
print()
print(f'Os numeros únicos digitados são: {sorted(lista)}')
print()
