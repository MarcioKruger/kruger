print('++-- \033[1;35;43mPROGRESSÃO ARITMÉTICA (PA). \033[m--++')
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = t
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=(' -> '))
    termo = termo + r
    cont = cont + 1
print(' ' * 20)
op = 1
while op != 0:
    op = int(input('Mostrar mais [ 1 ] ou parar [ 0 ]: '))
    if op == 1:
        t = int(input('Primeiro termo: '))
        r = int(input('Razão da PA: '))
        termo = t
        cont = 1
        while cont<= 10:
            print('{}'.format(termo), end=(' -> '))
            termo = termo + r
            cont = cont + 1
        print(' ' * 20)
print('ACABOU')
