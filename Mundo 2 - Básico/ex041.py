import datetime
print('-=-' * 30)
print('++-- \033[1;30;46mCLASSIFICAÇÃO DE ATLETAS!!! \033[m--++')
print('*' * 35)
ano = int(input('Digite o ano de nascimento do atleta: '))
print('*' * 35)
anoatual = datetime.datetime.now().year
anoatleta = anoatual - ano
if anoatleta <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM.'.format(anoatleta))
elif anoatleta > 9 and anoatleta <= 14:
    print('O atleta tem {} anos e está na cateegoria INFANTIL.'.format(anoatleta))
elif anoatleta > 14 and anoatleta <= 19:
    print('O atleta tem {} anos e está na categoria JÚNIOR.'.format(anoatleta))
elif anoatleta > 19 and anoatleta <=25:
    print('O atleta tem {} anos e está na categoria SÊNIOR.'.format(anoatleta))
elif anoatleta > 25:
    print('O atleta tem {} anos e está na categoria MASTER.'.format(anoatleta))
print('*' * 35)
print('-=-' * 30)
