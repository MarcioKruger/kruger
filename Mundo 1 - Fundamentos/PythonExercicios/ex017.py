import math
print('+' * 70)
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('a hipotenusa do triangulo é {:.2f}'.format(h))
print('-' * 70)
