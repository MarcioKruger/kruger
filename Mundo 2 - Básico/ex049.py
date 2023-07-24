print('++-- \033[1;35;43mTABUADA!!! \033[m--++')
t = float(input('Digite o numero da tabuada: '))
for c in range(1, 11):
    print('{} x  {} = {}'.format(t, c, t * c))
