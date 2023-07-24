print('===' * 20)
print('     ++++++++++ UNINDO DICIONÁRIOS E LISTAS +++++++++')
print('===' * 20)
lista = []
soma = media = 0
while True:
    pessoa = {}
    nome = str(input('Nome: '))
    pessoa['Nome']  = nome
    sexo = ""
    while sexo not in ['m', 'f']:
        sexo = str(input('Digite o sexo: ')).lower()
        pessoa['Sexo'] = sexo
    idade = int(input('Idade: '))
    pessoa['Idade'] = idade
    soma += pessoa['Idade']
    lista.append(pessoa)
    continuar = ""
    while continuar not in ['N', 'S']:
        continuar = input("Deseja continuar cadastrando? (S/N): ").upper()
    if continuar != 'S':
        break
quantidade = len(lista)
print('===' * 20)
print(lista)
media = soma / len(lista)
print(pessoa['Sexo'])
print(f'A) A média de idade é: {media:5.2f} anos.')
print(f'B) Foram cadastradas {quantidade} pessoas.')
print('C) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['Sexo'] in 'f':
        print(f'{p["Nome"]}', end='  ')
print()
print('D) Lista da pessoas que estão acima da média de idade: ')
for f in lista:
    if p['Idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('===' * 20)
print('--- ENCERRADO ---')
print()
