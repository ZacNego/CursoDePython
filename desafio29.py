'''vm = float(input('Velocidade limite é 80k/h, a cada km acima irá custa R$ 7.00\nDigite sua velocidade: '))
m = 7*(vm-80)
if vm >80:
    print('Multa R${:.2f}'.format(m))'''
velocidade = float(input('Qual é a velocidade atual do carro: '))
if velocidade>80:
    print('\033[1;31mMULTADO\033[m, você excedeu a velocidade que é de 80Km/h')
    multa = (velocidade-80)*7
    print('Você deve pagar uma multa de \033[0;36mR${:.2f}\033[m'.format(multa))
print('Tenha um bom dia, dirija com segurança')