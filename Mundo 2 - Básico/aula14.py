'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? S/N: ')).upper()
print('FIM!')'''
n= 1
par = 0
impar = 0
while n != 0:
    n= int(input('Digite um valor: '))
    if n% 2:
        par = par + 1
    else:
        impar = impar + 1
print('Você digitou {} numeros pares e {} numeros ímpares.'.format(par, impar))
