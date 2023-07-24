print('++-- \033[1;35;43mCONTAGEM DE VOGAIS. \033[m--++')
lista = ('caneca', 'copo', 'caneta', 'carro', 'moto', 'cama', 'sofa', 'telha', 'martelo', 'serrote', 'prego')
print('===' * 15)
for p in lista:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
print()
print('===' * 15)
