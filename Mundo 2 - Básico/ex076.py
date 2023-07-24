print('++-- \033[1;35;43mLISTA DE PRODUTOS E PREÇOS. \033[m--++')
lista = (str(input('Produto: ')), float(input('Preço: R$ ')), str(input('Produto: ')), float(input('Preço: R$ ')), str(input('Produto: ')), 
             float(input('Preço: R$ ')), str(input('Produto: ')), float(input('Preço: R$ ')), 
             str(input('Produto: ')), float(input('Preço: R$ ')))
print('----' * 15)
print(f'{"LISTA DE PREÇOS":^50}')
print('----' * 15)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end="")
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('----' * 15)
