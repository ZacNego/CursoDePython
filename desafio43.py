peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso/(altura**2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('Você está com peso IDEAL')
elif 25 <= imc <= 30:
    print('Você está com SOBREPESO')
elif 30 <= imc <= 40:
    print('Você está em OBESIDADE, cuidado')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
