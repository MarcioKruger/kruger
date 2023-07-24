print('++-- \033[1;35;43mUSANDO O COMANDO [BREAK]. \033[m--++')
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print(f'A soma dos números é: {s}.')
