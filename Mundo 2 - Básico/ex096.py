print('===' * 15)
print('       --- CÁLCULO DE ÁREA ---')
print('===' * 15)
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno com {comprimento:.2f} de comprimento e {largura:.2f} largura é {area:.2f} m²')


largura = float(input('Digite a Largura do terreno: '))
comprimento = float(input('Digite o comprimento do terrreno: '))
area(largura, comprimento)
print()