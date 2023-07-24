print('++-- \033[1;36;42mAnálise completa. \033[m--++')
soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulheres_menos_20 = 0
for i in range(1, 5):
    print('----- {}ª Pessoa -----'.format(i))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    soma_idade = soma_idade + idade
    media_idade = soma_idade / i
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
print('A média de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_homem_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulheres_menos_20))
