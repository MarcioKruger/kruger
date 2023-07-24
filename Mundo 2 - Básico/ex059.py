import time
n1 = float(input('Primeiro numero: '))
n2 = float(input('Segundo numero: '))
time.sleep(1)
op = 0
while op != 5:
    op = int(input('''                1: Somar
                2: Multiplicar
                3: Maior
                4: Novos numeros
                5: Sair
        '''))
    if op == 1:
        r = n1 + n2
        print('A soma de {} + {} : {}.'.format(n1, n2, r))
        time.sleep(1)
    elif op == 2:
        r = n1 * n2
        print('A multiplicação de {} * {} : {}.'.format(n1, n2, r))
        time.sleep(1)
    elif op == 3:
        if n1 > n2:
            print('O maior é {}'.format(n1))
            time.sleep(1)
        else:
            print('O maior é {}'.format(n2))
            time.sleep(1)
    elif op == 4:
        time.sleep(1)
        print('Digite novamente os numero!')
        n1 = float(input('Primeiro numero: '))
        n2 = float(input('Segundo numero: '))
        time.sleep(1)
    else:
        print('Opção inválida. TENTE Novamente:')
        time.sleep(1)
        op = int(input('''                1: Somar
                2: Multiplicar
                3: Maior
                4: Novos numeros
                5: Sair
        '''))

print('FECHANDO ... ')
time.sleep(2)
print('Programa fechado. Volte sempre!')
    