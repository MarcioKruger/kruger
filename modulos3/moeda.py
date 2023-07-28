def metade(num=0, formato=False):
    met = num / 2
    return met if formato is False else moeda(met)


def dobro(num=0, formato=False):
    dob = num * 2
    return dob if formato is False else moeda(dob)


def diminuir(d=0, formato=False):
    dim = d - (d * 0.10)
    return dim if formato is False else moeda(dim)


def aumentar(a=0, formato=False):
    aum = a + (a * 0.10)
    return aum if formato is False else moeda(aum)


def moeda(num=0, moeda = 'R$ '):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num=0, red=0, aum=0):
    texto = 'RESUMO DO VALOR'
    print('-' * 38)
    print(texto.center(38))
    print('-' * 38)
    dob = dobro(num)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{moeda(dob)}')
    print(f'Metado od preço: \t{metade(num, True)}')
    print(f'10% menos do preço: \t{diminuir(num, True)}')
    print(f'10% mais do preço: \t{aumentar(num, True)}')
    print('-' * 38)

