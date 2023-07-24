print('++-- \033[1;35;43mPROGRESSÃO ARITMÉTICA (PA). \033[m--++')
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=(' -> '))
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos vc quer mostrar mais: '))
print('FIM - Progressão Finalizada com {} termos mostrados.'.format(total))
