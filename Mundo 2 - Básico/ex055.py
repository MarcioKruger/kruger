print('++-- \033[1;36;42mMAIOR E MENOR PESO. \033[m--++')
pesos = []
for i in range(1, 6):
    peso = int(input('Digite o peso da pessoa {}: KG '.format(i)))
    pesos.append(peso)
menor = min(pesos)
maior = max(pesos)
print('O maior peso digitado foi {} KG e o menor foi {} KG.'.format(maior, menor))
