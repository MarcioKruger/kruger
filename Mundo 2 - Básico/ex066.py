print('++-- \033[1;35;43mSOMANDO VÁRIOS NÚMEROS. \033[m--++')
n = s = cont = 0
while True:
    n = int(input('Digite um número (999 PARA PARAR): '))
    if n == 999:
        break
    cont = cont +1
    s = s + n
print(f'Você digitou {cont} números e a soma deles é: {s}.')
