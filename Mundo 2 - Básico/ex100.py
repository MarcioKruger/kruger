import random
print('===' * 15)
print('       --- FUNÇÕES PARA SORTEAR E SOMAR ---')
print('===' * 15)
def sorteia():
    numeros = []
    for i in range(5):
        numSort = random.randint(1, 100)
        numeros.append(numSort)
    return numeros


def somaPar(num):
    soma = 0
    for numero in num:
        if numero % 2 ==0:
            soma = soma + numero
    return soma


sorteados = sorteia()
print(f'Os numeros sorteados foram : {sorteados} ')
print('=.=' * 15)
print('A soma dos numeros pares são: ', end='')
pares = somaPar(sorteados)
print(pares)
print('=.=' * 15)
print()
