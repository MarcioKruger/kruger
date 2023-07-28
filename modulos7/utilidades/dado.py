import re


def leiaDinheiro(msg):
    while True:
        valor = input(msg)
        valor_limpo = re.sub(r'[^\d.,]', '', valor)
        if not valor_limpo.replace(',', '').replace('.', '').isdigit():
            print("Valor inválido. Digite um valor monetário válido.")
            continue
        partes_decimais = valor_limpo.split(',')
        if len(partes_decimais) > 1 and len(partes_decimais[1]) > 2:
            print("Valor inválido. Digite no máximo duas casas decimais.")
            continue
        return float(valor_limpo.replace(',', '.'))

