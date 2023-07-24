print('++-- \033[1;35;43mLEITUTA DE PALÍNDROMO. \033[m--++')
f = str(input('Escreva a frase: ')).strip().upper()
se = f.replace(' ','')
fi = se[::-1]
if se == fi:
    print('a frase "{}" é um Palíndromo de "{}"'.format(fi, f))
else:
    print('A frase não é Palíndromo')
