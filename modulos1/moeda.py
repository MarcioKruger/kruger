def metade(num=0):
    met = num / 2
    return met


def dobro(num=0):
    dob = num * 2
    return dob


def diminuir(d=0):
    dim = d - (d * 0.10)
    return dim


def aumentar(a=0):
    aum = a + (a * 0.10)
    return aum


def moeda(num=0, moeda = 'R$ '):
    return f'{moeda}{num:.2f}'.replace('.', ',')
