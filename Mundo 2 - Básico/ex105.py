print('===' * 15)
print('       --- ANALISANDO E GERANDO DICIONÁRIOS ---')
print('===' * 15)


def notas(n):
    """
    A função notas(), recebe as notas de vários alunos, e retorna os valores:
    1 - A quantidade de notas recebidas.
    2 - A maior nota da turma.
    3 - A menor nota da turma.
    4 - A media da turma.
        Por fim, a função pede ao usuário se ele quer ver a situação geral da turma.    
    """
    dict = {}
    lista = []
    while True:
        n = float(input('Digite a nota: '))
        lista.append(n)
        dict['nota'] = lista
        lista.clear
        p = str(input('Continuar? S/N: ')).upper().split()[0]
        if p == 'N':
            break
    print(f'As Notas ta turma são respectivamente: {dict["nota"]}')
    print(f'A) Quantidade de notas: {len(dict["nota"])}')
    print(f'B) A maior nota é: {max(dict["nota"])}')
    print(f'C) A menor nota é: {min(dict["nota"])}')
    numeros = dict['nota']
    media = sum(numeros) / len(numeros)
    print(F'd) A media da turma é: {media:.1f}')
    perg = str(input('Desja ver a situação da turma: S/N ')).upper().split()[0]
    if perg == 'S':
        if media >= 7:
            print('D) Turma BOA.')
        elif media < 5:
            print('D) Turma RAZOÁVEL.')
        else:
            print('Turma em RUIM.')
    perg1 = str(input('Desja ver a DocString da função? S/N ')).upper().split()[0]
    if perg1 == 'S':
        print()
        help(notas)
    

#Programa principal
notas(notas)
print()
