print('-=-' * 20)
s = float(input('Digite o valor do salário atual: R$ '))
if s > 1250.00:
    print('Seu novo salário será R$ {:.2f}'.format((s * 0.10) + s))
if s <= 1250.00:
    print('Seu novo salário seerá R$ {:.2f}'.format((s * 0.15) + s))
print('-=-' * 20)
