print('-=-' * 30)
print('++-- \033[1;35;43mANALISE DE UMA EXPRESSÃO. \033[m--++')
print('-=-' * 30)
exp = str(input('Digita a expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop() 
        else:
            pilha.append(')')
            break
print('-=-' * 30)
if len(pilha) == 0:
    print('Sua espressão esta CORRETA.')
else:
    print('Sua expressão está ERRADA.')
print('-=-' * 30)
print()
