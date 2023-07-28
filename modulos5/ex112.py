from utilidades import moeda, dado
print('===' * 15)
print('       --- MOEDAS EM PYTHON ---')
print('===' * 15)

numero = dado.leiaDinheiro('Digite o valor: R$ ')
moeda.resumo(numero)
