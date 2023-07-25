print('===' * 15)
print('       --- UM PRINT ESPECIAL ---')
print('===' * 15)

def escreva(texto):
    t = len(texto) + 4
    print('~' * t)
    print(f'  {texto}')
    print('~' * t)

texto = str(input('Escreva o texto: '))
escreva(texto)
