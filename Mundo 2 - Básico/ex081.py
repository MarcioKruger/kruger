print('++-- \033[1;35;43mANALISANDO VALORES DE UMA LISTA. \033[m--++')
print('-=-' * 30)
lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Continuar? S/N: ')).upper().split()[0]
    if resposta == 'N':
        break
print('-=-' * 30)
print(f'números digitados: {lista}')
print(f'Foram digitados {len(lista)} numeros.')
decresc = sorted(lista, reverse=True)
print(f'Lista em ordem decrescente: {decresc}')
if 5 not in lista:
    print('O numero 5 não foi digitado e não está na lista.')
else:
    print('O número 5 foi digitado e está na lista')
print('-=-' * 30)
print()
