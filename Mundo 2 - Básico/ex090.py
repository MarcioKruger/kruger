print('-=-' * 15)
print('++-- \033[1;35;43mMÉDIA ESCOLAR. \033[m--++')
print('-=-' * 15)
lista = {}
nome = str(input('Nome do aluno: '))
lista['nome'] = nome
media = float(input(f'Média do {(lista["nome"])}: '))
lista['media'] = media
if media >= 7:
    lista['situação'] = 'Aprovado'
elif media >= 5 and media < 7:
    lista['situação'] = 'Em Recuperação'
else:
    lista['situação'] = 'Reprovado'
print('-=-' * 15)
for k, v in lista.items():
    print(f' -> {k} é igual a: {v}')
print('-=-' * 15)
print()