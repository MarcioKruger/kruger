import time
print('===' * 15)
print('       --- FUNÇÃO DE CONTADOR ---')
print('===' * 15)

def contador(i, f, p):
    time.sleep(2.5)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ', flush=True)
            cont += p
            time.sleep(0.5)
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end=' ', flush=True)
            cont -= p
            time.sleep(0.5)
        print('FIM')
        

#Exercício A - contagem de 1 até 10, de 1 em 1
print('A) Contagem de de 1 até 10, de 1 em 1: ')
contador(1, 10, 1)
print()
#Exercício B - Contagem 10 ate 0, de 2 em 2
print('B) Contagem de 10 até 0, de 2m em 2: ')
contador(10, 0, 2)
print()
#Exerccio C - Contagem personalizada
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
print('C) Uma contagem personalizada: ')
contador(inicio, fim, passo)
print()
