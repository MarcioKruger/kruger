print('-=-' * 15)
print('++-- \033[1;35;43mMÉDIA ESCOLAR. \033[m--++')
print('-=-' * 15)
lista = []
temp = []
media = n1 = n2 = 0
while True:
    nome = str(input('Nome do aluno: ')).upper()
    temp.append(nome)
    nota1 = float(input('Nota 1: '))
    temp.append(nota1)
    nota2 = float(input('Nota 2: '))
    temp.append(nota2)
    lista.append(temp[::])
    temp.clear()
    perg = str(input('Deseja continuar? S/N: ')).upper().split()[0]
    if perg == 'N':
        break
print(lista)
for c in lista:
    print(f'O aluno {c[0]} obteve a média: {(c[1] + c[2]) / 2}.')
while True:
    perg = str(input('Deseja mostra as notas individuais? S/N: ')).upper().split()[0]
    if perg == 'N':
        break
    mostrar = str(input('Aluno: ')).upper()
    for c in lista:
        if c[0] == mostrar:
            n1 = c[1]
            n2 = c[2]
            print(f'As notas de {c[0]} são {n1} e {n2}.')
print()
print('PROGRAMA ENCERRADO!!!')     
print()
