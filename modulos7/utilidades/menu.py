from utilidades import moeda

def opcao1(op):
    print(lin())
    print('\033[1;35mPESSOAS CADASTRADAS\033[m'.center(45))
    print(lin())


def opcao2(op):
    print(lin())
    print('\033[1;35mCADASTRAR PESSOA\033[m'.center(45))
    print(lin())


def opcao3(op):
    print(lin())
    print('\033[1;35mSAINDO DO SISTEMA...\033[m'.center(45))
    print(lin())

def lin(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(lin())
    print(txt.center(42))
    print(lin())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c = c +1
    print(lin())
    op = moeda.leiaInt('\033[31mOpção: \033[m')
    return op

