import random
print('++-- \033[1;35;43mJOGO - PAR OU ÍMPAR!!!. \033[m--++')
cont = perdeu = 0
while True:
    n = int(input('Escolha um número: '))
    a = str(input('Escolha par ou ímpar: [ P/I ]: ')).upper().strip()[0]
    while a not in 'PI':
        a = str(input('Escolha par ou ímpar: [ P/I ]: ')).upper().strip()[0]
    pc = random.randrange(0, 10)
    resol = n + pc
    poui = resol % 2
    if a == 'P' and poui == 0:
        print(f'Você Escoleu o numero: {n} e escolheu {a}AR. O PC escolheu {pc}, e deu o valor {resol}: PAR! -  Você Ganhou!!')
        cont = cont + 1
    elif a == 'P' and poui ==  1:
        perdeu = 1
        print(f'Você Escoleu o numero: {n} e escolheu {a}AR. O PC escolheu {pc}, e deu o valor {resol}: ÍMPAR - Você Perdeu!!')
        if perdeu == 1:
            break
    elif a == 'I' and poui == 0:
        perdeu = 1
        print(f'Você Escoleu o numero: {n} e escolheu {a}MPAR. O PC escolheu {pc}, e deu o valor {resol}: PAR - Você Perdeu!!')
        if perdeu == 1:
            break
    elif a == 'I' and poui == 1:
        print(f'Você Escoleu o numero: {n} e escolheu {a}MPAR. O PC escolheu {pc}, e deu o valor {resol}: ÍMPAR! -  Você Ganhou!!')
        cont = cont + 1
print(f'Você ganhou {cont} vez(es).')
