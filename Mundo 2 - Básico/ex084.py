print('-=-' * 15)
print('++-- \033[1;35;43mLISTA COMPOSTA E ANÁLISE DE DADOS. \033[m--++')
print('-=-' * 15)
temp = []
princ = []
maispeso = maisleve = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        maispeso = maisleve = temp[1]
    else:
        if temp[1] > maispeso:
            maispeso = temp[1]
        if temp[1] < maisleve:
            maisleve = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Continuar? S/N: ')).upper().split()[0]
    if resp == 'N':
        break
print('-=-' * 15)
print(f'Quantidade de pessoas cadastradas: {len(princ)}')
print(f'O maior peso foi {maispeso} Kg, peso de', end=' ')
for p in princ:
    if p[1] == maispeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'\bO menor peso foi {maisleve} Kg, peso de  ', end= '')
for p in princ:
    if p[1] == maisleve:
        print(f'[{p[0]}]  ', end=' ')
print()
print('-=-' * 15)
print()
