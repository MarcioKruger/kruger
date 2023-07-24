print('++-- \033[1;35;43mPROGRESSÃO ARITMÉTICA (PA). \033[m--++')
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
cont = 1
termo = t
while cont <= 10:   
    print('{}'.format(termo), end=(' -> '))
    termo = termo + r
    cont = cont + 1
print('ACABOU')
