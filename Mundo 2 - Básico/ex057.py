print('++-- \033[1;36;42mAnálise do sexo. \033[m--++')
sexo = str(input('Qual seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados iválidos. Informe seu sexo [M/F]: ')).upper().strip()[0]
print('Seu sexo é {}.'.format(sexo))
