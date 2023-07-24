print('-=-' * 20)
v = float(input('Digite a velocidade do carro: '))
va = v - 80
m = va * 7
if v > 80:
    print('Sua velovidade foi de {:.2f} km/h e ultrapssou 80 km/h.'.format(v))
    print('Sua multa será de R$ {:.2f}.'.format(m))
else:
    print('Sua velocidade esta dentro do limite!')
print('-=-' * 20)
