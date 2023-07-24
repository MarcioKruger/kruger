from datetime import datetime
print('-=-' * 30)
print('++-- \033[1;31;40mALISTAMENTO MILITAR \033[m--++')
print('*' * 35)
ano = int(input('Digite seu ano de nascimento: '))
sexo  = str(input('Seu sexo é ( M) - Masculino ou ( F ) - Feminino: ')).upper()
anoatual = datetime.now().year
falta = anoatual - ano
print('*' * 35)
if falta > 18 and sexo == 'M':
    passou = falta - 18
    print('Você tem {} anos! Ja Passou {} anos de se alistar'.format(falta, passou))
elif falta < 18 and sexo == 'M':
    faltapara = (ano + 18) - anoatual
    print('Você tem {} anos e ainda falta(m) {} ano(s) para se alistar'.format(falta, faltapara))
elif falta == 18 and sexo == 'M':
    print('Você tem {} e deve se alistar agora'.format(falta))
elif sexo == 'F':
    print('Você é do sexo FEMININO e não precisa se alistar.')
print('*' * 35)
print('-=-' * 30)
