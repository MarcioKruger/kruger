print('++-- \033[1;35;43mANÁLISE DE DADOS EM UMA TUPLA. \033[m--++')
num = (int(input('Digite o numero 1: ')), int(input('Digite o numero 2: ')), int(input('Digite o numero 3: ')), int(input('Digite o numero 4: ')))
print('Foram digitados os numeros:', num)
if 3 in num:
    print(f'o numero 3 esta na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'o número 9 aparece {num.count(9)} vezes')
print('Os números pares são: ', end='')
for par in num:
    if par % 2 == 0:
        print(par, end='   ')
