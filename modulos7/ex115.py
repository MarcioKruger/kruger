import time
from utilidades import moeda, menu
while True:
    resposta = menu.menu(['Lista pessoas', 'Cadastrar pessoa', 'SAIR'])
    if resposta == 1:
        menu.opcao1(1)
    elif resposta == 2:
        menu.opcao2(2)
    elif resposta == 3:
        break
    time.sleep(2)
print()
