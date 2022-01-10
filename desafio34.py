salario = float(input('Qual o sálario do funcionário? R$'))
if salario <= 1250.00:
    novo = salario * 1.15
else:
    novo = salario * 1.10
print('Quem ganhava \033[4;31mR${:.2f}\033[m passa a ganhar \033[4;36mR${:.2f}\033[m'.format(salario, novo))