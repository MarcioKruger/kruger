import time

def contador(inicio, fim, passo):
    if passo == 0:
        print("O passo não pode ser igual a zero.")
    elif passo < 0:
        passo *= -1

    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
            time.sleep(1)  # Pausa por 1 segundo
        print("FIM!")
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
            time.sleep(1)  # Pausa por 1 segundo
        print("FIM!")

inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
passo = int(input("Digite o passo: "))

print("\nContagem personalizada:")
contador(inicio, fim, passo)
