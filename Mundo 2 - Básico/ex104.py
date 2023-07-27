print('===' * 15)
print('       --- ENTRADA DE DADOS EM PYTHON ---')
print('===' * 15)


def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Digite um valor numérico válido.")



# Teste da função
n = leiaInt('Digite um número inteiro: ')
print(f'O número digitado foi: {n}')
print()
