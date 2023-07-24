print('-=-' * 30)
print('++-- \033[1;37;46mCALCULADORA DE ÍNDiCE DE MASSA CORPORAL(IMC)!!! \033[m--++')
print('*' * 35)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
print('*' * 35)
imc = peso / (altura ** 2)
if imc < 18.5:
    print('seu IMC é {:.1f}, por isso está ABAIXO DO PESO.'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC é {:.1f}, por isso está com o PESO IDEAL.'.format(imc))
elif imc >= 25 and imc <30:
    print('seu IMC é {:.1f}, por isso está com SOBREPESO.'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f}, por isso está com OBESIDADE.'.format(imc))
elif imc >= 40:
    print('Seu IMC é {:.1f}, por isso está com OBESIDADE MORBIDA.'.format(imc))
print('*' * 35)
print('-=-' * 30)
