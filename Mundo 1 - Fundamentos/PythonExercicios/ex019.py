print('+' * 70)
import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('quarto aluno: ')
lista = [a1, a2, a3, a4]
s = random.choice(lista)
print('O aluno escolhido foi: {}'.format(s))
print('-' *70)
