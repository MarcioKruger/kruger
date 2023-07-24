print('++-- \033[1;35;43mSEQUENCIA DE FIBONACCI. \033[m--++')
n = int(input('Digite o numero paraachar a sequencia de FIBONACCI: '))
def fibonacci_sequence(n):
    fib = [0, 1]  # Inicializando a sequência com os primeiros dois números (0 e 1)
    while fib[-1] <= n:  # Continuar adicionando números até que o próximo número seja maior que n
        next_fib = fib[-1] + fib[-2]  # Calcula o próximo número da sequência
        if next_fib <= n:
            fib.append(next_fib)  # Adiciona o próximo número se for menor ou igual a n
        else:
            break  # Encerra o loop se o próximo número exceder n
    return fib
result = fibonacci_sequence(n)
print(result)
