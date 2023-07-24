import random
print('++-- \033[1;35;43mMAIORES E MENORES NUMEROS EM UMA TUPLA. \033[m--++')
num = (random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000))
print('Os numeros sorteados foram: ', end='')
for c in num:
    print(f'{c} ', end='')
print(f'\nO maior numero da lista é: {max(num)}')
print(f'O menor numero da lista é: {min(num)}')
