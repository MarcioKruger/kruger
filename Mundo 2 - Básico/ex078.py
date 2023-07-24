print('++-- \033[1;35;43mMENOR E MAIOR VALOR EM UMA LISTA. \033[m--++')
lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o valor para a posição {c}: ')))
print(f'Os valores digitados foram: {lista}')
print(f'O MAIOR valor digitado foi {max(lista)} e está na posição ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}... ', end='')
print()
print(f'O MENOR valor digitado foi {min(lista)} e está na posição ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ', end='')
print()
