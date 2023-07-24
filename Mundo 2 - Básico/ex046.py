import time
print('{:=^100}'.format(' VIVA O ANO NOVO. '))
tempo = int(input('Digite o tempo de contagem: '))
for c in range(tempo, -1, -1):
    print(c)
    time.sleep(1)
print('BBBUUMMMMMMMMM')
