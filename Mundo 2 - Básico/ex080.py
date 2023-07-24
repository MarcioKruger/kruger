print('++-- \033[1;35;43mINSERINDO VALORES NUMÉRICOS NA ORDEM CORRETA EM UMA LISTA. \033[m--++')
print('-=-' * 30)
valores = []
for c in range(5):
    valor = int(input("Digite um valor numérico: "))
    if not valores:
        valores.append(valor)
    else:
        inserido = False
        for i, v in enumerate(valores):
            if valor < v:
                valores.insert(i, valor)
                inserido = True
                break
        if not inserido:
            valores.append(valor)
print('-=-' * 30)
print(f'Lista ordenada: {valores}')
print()
