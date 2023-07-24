print('-=-' * 20)
d = float(input('Digite a distância da viagem em Km: '))
if d > 200:
    print('O preço da passagem é R$ {:.2f}.'.format(d * 0.45))
else:
    print('O preço da passagem é R$ {:.2f}.'.format(d * 0.50))
print('-=-' * 20)
