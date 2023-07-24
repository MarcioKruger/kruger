preco = float(input("qual é o preço do produto: "))
d = preco * 0.05
np = preco - d
print('o desconto de 5% no valor de R${:.2f} é: R${:.2f}, o novo preço é: R${:.2f}'.format(preco, d, np))
