valor_saque = int(input("Digite o valor a ser sacado: R$"))

cedulas = [50, 20, 10, 1]
quantidades_cedulas = [0, 0, 0, 0]

for i in range(len(cedulas)):
    quantidade_cedulas = valor_saque // cedulas[i]
    valor_saque = valor_saque % cedulas[i]
    quantidades_cedulas[i] = quantidade_cedulas

print("\nQuantidade de cédulas:")
for i in range(len(cedulas)):
    print(f"Cédulas de R${cedulas[i]}: {quantidades_cedulas[i]}")
