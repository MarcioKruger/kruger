print('+' * 70)
nome = str(input('Digite seu nome completo: ')).strip()
m = nome.upper()
mi = nome.lower()
q = nome.split()
l = len(q[0])
lt = nome.count(' ')
cl = len(nome) - lt
print('Letras maiusculas: {}'.format(m))
print('Letras minusculas: {}'.format(mi))
print('Quantidade de letras do primeiro nome: {}'.format(l))
print('Quantidade de carcteres: {}'.format(cl))
print('-' * 70)
