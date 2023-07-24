print('-=-' * 15)
print('++-- \033[1;35;43mLISTA COM PARES E ÍMPARES. \033[m--++')
print('-=-' * 15)
principal = [[], []]
for i in range(1, 8):
    valor = int(input(f'digite o numero {i}: '))
    if valor % 2 == 0:
        principal[0].append(valor)
    else:
        principal[1].append(valor)
print(principal)
parordenado = sorted(principal[0])
imparordenado = sorted(principal[1])
print(f'Os numeros pares são: {parordenado}')
print(f'Os numeros ímpares são: {imparordenado}')
