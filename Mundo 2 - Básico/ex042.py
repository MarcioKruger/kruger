print('-=-' * 30)
print('++-- \033[1;37;46mCLASSIFICAÇÃO DE TRIÃNGULOS!!! \033[m--++')
print('*' * 35)
r1 = float(input('Primeiro segmento da reta: '))
r2 = float(input('Segundo segmento da reta: '))
r3 = float(input('Terceiro segmento da reta: '))
print('*' * 35)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento {}, {} e {} PODEM FORMAR triâmgulo.'.format(r1, r2, r3))
    if r1 == r2 and r2 == r3:
        print('É um triângulo EQUILÁTERO.')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('É um triângulo ESCALENO')
    else:
        print('É um triângulo ISÓSELES')
else:
    print('Os segmentos {}, {} e {} NÃO PODEM FORMAR triângulo.'.format(r1, r2, r3))
print('*' * 35)
print('-=-' * 30)
