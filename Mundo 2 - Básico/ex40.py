print('-=-' * 30)
print('++-- \033[1;30;44mMEDIA ESCOLAR COM RESULTADO \033[m--++')
print('*' * 35)
n1 = float(input('Qual é a primeira nota: '))
n2 = float(input('Qual é a segunda nota: '))
m = (n1 + n2) / 2
print('*' * 35)
if m < 5:
    print('Sua média foi {} e você foi REPROVADO'.format(m))
elif m >= 7:
    print('Sua média foi {} e você está APROVADO!'.format(m))
else:
    print('Sua média foi {} e você está de RECUPERAÇÃO'.format(m))
print('*' * 35)
print('-=-' * 30)
