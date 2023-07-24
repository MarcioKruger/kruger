print('++-- \033[1;35;43mNUMEROS PRIMOS. \033[m--++')
cont = 0
num = int(input('digite o numero: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end=(' '))
        cont = cont + 1
    else:
        print('\033[35m', end=(' '))
    print('{}'.format(c), end=' ')
print('\n\033[m O número {} foi divisível {} vezes.'.format(num, cont))
if cont == 2:
    print('e por isso ele É PRIMO.')
else:
    print('e por isso ele NÃO É PRIMO.')
