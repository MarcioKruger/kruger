import datetime
print('-=-' * 15)
print('      ++-- \033[1;35;43mCADASTRO DE TRABALHADOR. \033[m--++')
print('-=-' * 15)
trabalhador = {}
nome = str(input('Nome: '))
trabalhador['Nome'] = nome
nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - nascimento
trabalhador['Idade'] = idade
carteira = int(input('Carteira de Trablaho (0 se não tem): '))
trabalhador['Carteira'] = carteira
if carteira != 0:
    contratacao = int(input('Ano de contratação: '))
    trabalhador['Contratacao'] = contratacao
    aposentadoria = ((contratacao + 35) - (datetime.datetime.now().year)) + idade
    trabalhador['Aposentadoria'] = aposentadoria
    salario = float(input('Salário: '))
    trabalhador['Salario'] = salario
print('===' * 12)
for k, v in trabalhador.items():
    print(f' -> {k}: {v}')
print('===' * 12)
print()
