print('-=-' * 20)
r1 = float(input('Primeiro segmento da reta: '))
r2 = float(input('Segundo segmento da reta: '))
r3 = float(input('Terceiro segmento da reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmento {}, {} e {} PODEM FORMAR triâmgulo.'.format(r1, r2, r3))
else:
    print('Os segmentos {}, {} e {} NÃO PODEM FORMAR triângulo.'.format(r1, r2, r3))
print('-=-' * 20)
