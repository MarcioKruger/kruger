print('-=-' * 30)
print('-=-' * 30)
print('++-- \033[1;33;41mCOMPARADOR NUMÉRICO \033[m--++')
print('*' * 35)
n1 = int(input('Primeiro numero: '))
n2 = int(input('segundo numero: '))
print('*' * 35)
if n1 > n2:
    print('O primeiro valor {}, é maior'.format(n1))
elif n2 > n1:
    print('O segundo valor: {} é maior'.format(n2))
else:
    print('Não existe valor maior: {} e {} são iguais'.format(n1, n2))
print('*' * 35)

print('-=-' * 30)
print('-=-' * 30)
