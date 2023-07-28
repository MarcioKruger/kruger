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
