print('++-- \033[1;35;43mEscrita de números por extenso. \033[m--++')
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Quatroze', 'Quinze', 'Dezeseis', 'Dezesete', 
            'Dezoito', 'Dezenove', 'Vinte')
while True:
    ler = int(input('Digite um numero inteiro de 0 até 20: '))
    while ler not in range(0, 21):
        ler = int(input('tente novamente. Digite um numero inteiro de 0 até 20: '))
    print(f'Você digitou o núemro {numeros[ler]}')
    resposta = ' '
    while resposta not in 'SN':
        resposta = input("Deseja continuar? (s/n): ").upper().split()[0]
    if resposta == 'N':
        break
print('Final do programa')
