import time
from utilidades import arquivo, menu, moeda

arq = 'documento.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = menu.menu(['Lista pessoas', 'Cadastrar pessoa', 'SAIR'])
    if resposta == 1:
        menu.opcao1(1)
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        menu.opcao2(2)
        nome = str(input('Nome: '))
        idade = moeda.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        break
    time.sleep(2)
print()
