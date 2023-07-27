import datetime
print('===' * 15)
print('       --- FUNÇÕES PARA VOTAÇÃO ---')
print('===' * 15)


def voto(nascimento):
    anoatual = datetime.datetime.now().year
    idade = anoatual - nascimento
    if idade < 16:
        return 'Voto NEGADO, menos de 16 anos'
    elif 18 < idade >= 65:
        return 'Voto OPCIONAL, pessoas entre 16 e 18 anos e acima de 65 anos.'
    else:
        return 'Voto OBRIGATÓRIO, pessoas entre 18 e 65 anos'


def idade(ano):
    anoatual = datetime.datetime.now().year
    idade = anoatual - ano
    return idade


n = int(input('Digite o ano de nascimento: '))
idade(n)
voto(n)
print(f'A situação do voto de uma pessoas de {idade(n)} anos é: {voto(n)}')
