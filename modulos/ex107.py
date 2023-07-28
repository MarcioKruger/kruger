from moeda import dobro, metade, diminuir, aumentar
print('===' * 15)
print('       --- MÓDULOS EM PYTHON ---')
print('===' * 15)

numero = int(input('Digite o valor: R$ '))
dob = dobro(numero)
print(f'O dobro de {numero} é {dob}')
print(f'A metade de {numero} é {metade(numero)}')
print(f'10% de {numero} é {diminuir(numero)}')
print(f'Mais 10% de {numero} é {aumentar(numero)}')
