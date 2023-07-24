print('++-- \033[1;35;43mANÁLISE DE LISTA DE COMPRAS. \033[m--++')
total = totalmil = menor = cont = 0
barato = ''
while True:
    nome = input("Digite o nome do produto: " )
    preco = float(input("Digite o preço do produto: R$" ))
    total = total + preco
    cont = cont + 1
    if preco > 1000:
        totalmil = totalmil + 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = input("Deseja continuar? (s/n): ").upper().split()[0]
    if resposta == 'N':
        break
print(f'O total gasto na compra foi R$ {total}')
print(f'Quantidade de produtos acima de R$1000: {totalmil}')
print(f'Nome do produto mais barato: {barato}')
