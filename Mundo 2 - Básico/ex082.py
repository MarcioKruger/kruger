print('-=-' * 30)
print('++-- \033[1;35;43mBUSCANDO VALORES PARES E ÍMPARES EM UMA LISTA. \033[m--++')
print('-=-' * 30)
lista = []
par = []
impar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = str(input('Deseja continuar? S/N: ')).upper().split()[0]
    if resp == 'N':
        break
for i, valor in enumerate(lista):
    if valor % 2 == 0:
        par.append(valor)
    if valor % 2 == 1:
        impar.append(valor)
print('-=-' * 30)
print(f'A lista de números digitados é: {lista}')
print(f'Os numeros pares digitados dos foram: {par}')
print(f'Os numeros impares digitados foram: {impar}')
print('-=-' * 30)
print()
