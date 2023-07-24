n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
me = (n1 + n2) / 2
print('sua media foi {:.1f}'.format(me))
if me >= 6.0:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua média foi ruim. Estude mais!')
    