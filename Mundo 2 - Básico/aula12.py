nome = str(input('Qual seu nome? '))
if nome == 'Marcio':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Carlos' or nome == 'Joao':
    print('Seu nome é popuplar no Brasil')
elif nome in 'Ana Maria Monica':
    print('Que belo nome feminino!')
else:
    print('Seu nome é normal!')
print('Tenha um bom dia, {}!'.format(nome))
