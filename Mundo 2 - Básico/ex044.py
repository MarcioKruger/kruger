print('-=-' * 30)
print('{:=^100}'.format(' PROGRAMA DE VENDAS E DESCONTO. '))
print('*' * 35)
preço = float(input('Valor do produto: R$ '))
pag = int(input('''Qual a forma de pagamento? 
                [ 1 ] à vista dinheiro (10% de desconto):
                [ 2 ] À vista cartão(5% de desconto):
                [ 3 ] até 2x no cartão. Sem desconto:
                [ 4 ] 3x ou mais no cartão (20% de juros):
                Digite a opção: '''))
print('*' * 35)
if pag == 1:
    desc = preço - (preço * 0.10)
    print('Valor com 10% de desconto: R$ {:.2f}'.format(desc))
elif pag == 2:
    desc = preço - (preço * 0.05)
    print('Valor com 5% de desconto: R$ {:.2f}'.format(desc))
elif pag == 3:
    parc = (preço / 2)
    print('Duas parcelas de R$ {}, Valor total de R$ {:.2f}'.format(parc, preço))
elif pag == 4:
    parc = int(input('Quantas parcelas: '))
    prest = (preço / parc)
    prestaçao = (prest * 0.20) + prest
    pfinal = (prestaçao * parc)
    print('A quantidade de parcelas é {} no valor de R$: {:.2f}'.format(parc, prestaçao))
    print('O valor total será de R$ {:.2f}'.format(pfinal))
elif pag != 1 and pag != 2 and pag != 3 and pag != 4:
    print('Opção inválida. Tente Novamente!')
    print('*' * 35)
print('-=-' * 30)
