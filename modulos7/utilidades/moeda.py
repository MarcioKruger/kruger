def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mErro: Digite um valor inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário não digitou um valor.\033[m')
        else:
            return valor
        

def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print("Erro: Digite um valor real válido.")
            continue
        else:
            return valor

