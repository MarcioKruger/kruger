print('===' * 15)
print('       --- FUNÇÕES PARA FATORIAL ---')
print('===' * 15)


def fatorial(n, show=False):
    """-> Calcula o fatorial de um número.
    -parâmetro n: o número a ser calculado.
    - parâmetro Show: (opcional). Mostra ou não ao conta.
    - return: O valor fatorial de um número n.
"""
    fatorial = 1
    for i in range(1, n + 1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial *= i
    return fatorial

#Programa principal
print(fatorial(5))
help(fatorial)
