casa = float(input('Valor da casa:R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minino = salario *30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos))
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minino:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')