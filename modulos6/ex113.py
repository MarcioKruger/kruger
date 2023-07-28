from utilidades import moeda, dado
print('===' * 15)
print('       --- FUNÇÕES EM PYTHON ---')
print('===' * 15)

# Teste da função
inteiro = moeda.leiaInt('Digite um número inteiro: ')
real = moeda.leiaFloat('Digite um número flutuante: ')
print(f'O número INTEIRO digitado foi: {inteiro}, ', end='')
print(f'e número REAL digitado foi: {real}')
print()
