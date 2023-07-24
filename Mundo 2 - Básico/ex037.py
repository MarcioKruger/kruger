print('-=-' * 30)
print('-=-' * 30)
print('++-- \033[1;35;43mCONVERSOR NUMÉRICO \033[m--++')
print('*' * 35)
num = int(input('Digite o número: '))
base = int(input('Escolha 1= binário, 2= octal ou 3= hexadecimal: '))
print('*' * 35)
binario = bin(num)
octal = oct(num)
hexa = hex(num)
if base == 1:
    print('A base binária de {} é: {}'.format(num, binario[2::]))
elif base == 2:
    print('Abase octal de {} é: {}'.format(num, octal[2::]))
elif base == 3:
    print('A base hexadecimal de {} é: {}'.format(num, hexa[2::]))    
else:
    print('Opção inválida. Tente novamente.')
print('*' * 35)

print('-=-' * 30)
print('-=-' * 30)
