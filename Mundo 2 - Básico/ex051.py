print('++-- \033[1;35;43mPROGRESSÃO ARITMÉTICA (PA). \033[m--++')
t = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a Razão da Progressão Aritmética: '))
decimo = t + (10 - 1) * r
for c in range(t, decimo + r, r):
    print('{}'.format(c), end=(' -> '))
print('ACABOU')
