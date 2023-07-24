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
print("Matriz:")
for i in range(3):
    for j in range(3):
        print(matriz[i][j], end=' ')
    print()

