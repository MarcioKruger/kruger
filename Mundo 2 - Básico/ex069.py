print('++-- \033[1;35;43mANÁLISE DE DEDOS DO GRUPO!!!. \033[m--++')
homem = maior = mulhermenos = 0
print('-' * 20)
while True:
    idade = int(input('Digite a idade: '))
    print('-' * 20)
    sexo = str(input('Digite o sexo [ M/F]:' )) .upper() .split()[0]
    print('-' * 20)
    if sexo == 'F' and idade < 20:
        mulhermenos += 1
    if sexo == 'M':
        homem += 1
    if idade > 18:
        maior += 1
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [ M/F]:' )) .upper() .split()[0]
        r = str(input('Desja inserir mais um dado? [ S/N ]:' )) .upper() .split()[0]
    print('-' * 20)
    while r not in 'SN':
        r = str(input('Desja inserir mais um dado? [ S/N ]:' )) .upper() .split()[0]
    if r == 'N':
        break
print('+' * 40)
print(f'Maiores de idade: {maior}')
print(f'Homens cadastrados: {homem}')
print(f'Mulher(es) com menos de 20 anos: {mulhermenos}')
print('+' * 40)
print('FIM...')
