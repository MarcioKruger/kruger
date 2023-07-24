print('++-- \033[1;35;43mMostrando a tabuada. \033[m--++')
n =  0
while True:
    n = int(input('Digite um número (-1 PARA PARAR): '))
    if n < 0:
        break
    print(f'------ Tabuada do {n} -----')
    for c in range(1, 11):
        print(f'{n} x  {c} = {n * c}')
print('Pronto!')
