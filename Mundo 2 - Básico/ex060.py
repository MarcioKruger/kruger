print('=-=' * 14)
print('Cálculo do fatorial de um numero inteiro')
print('=-=' * 14)
num = int(input('Numero: '))
f = 1
i = num
print('Calculando {}! : '.format(num), end='')
while i > 0:
    print('{} '.format(i), end='')
    print('x ' if i > 1 else ' = ', end='')
    f = f * i
    i = i - 1
print('{}.'.format(f))
