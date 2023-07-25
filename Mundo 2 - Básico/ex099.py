print('===' * 15)
print('       --- FUNÇÃO PARA BUSCAR O MAIOR NÚMERO ---')
print('===' * 15)
def maior(numero):
    t = len(numero)
    m = max(numero)
    print(f'Foram informado {t} números e o maior é: {m}')
    

lista = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    perg = str(input('continuar? S/N: ')).upper().split()[0]
    if perg in 'N':
        break
maior(lista)
