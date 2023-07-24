print('-=-' * 15)
print('++-- \033[1;35;43mMATRIZES EM PYTHON. \033[m--++')
print('-=-' * 15)
# Criando uma matriz 3x3 preenchida com zeros
matriz = [[0 for _ in range(3)] for _ in range(3)]
# Preenchendo a matriz com valores lidos pelo teclado
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
# Exibindo a matriz na tela com a formatação correta
print('-=-' * 15)
print("Matriz:")
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=' ')
    print()
pares = []
col = []
maior = []
a = matriz[0]
for p in a:
    if p % 2 == 0:
        pares.append(p)
b = matriz[1]
for pa in b:
    if pa % 2 == 0:
        pares.append(pa)
c = matriz[2]
for par in c:
    if par % 2 == 0:
        pares.append(par)
print('-=-' * 15)
print(f'a soma dos pares da matriz é: {sum(pares)}')
col.append(matriz[0][2])
col.append(matriz[1][2])
col.append(matriz[2][2])
print(f'A soma dos valores da terceira coluna é: {sum(col)}')
maior.append(matriz[1][0])
maior.append(matriz[1][1])
maior.append(matriz[1][2])
print(f'O maior valor da segunda linha é: {max(maior)}')
print('-=-' * 15)
