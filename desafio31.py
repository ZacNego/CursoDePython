km = float(input('Qual é a distância da sua viagem: '))
print('Você está preste a começar uma viagem de {} Km'.format(km))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('E o preço de sua passagem será R${:.2f}'.format(preço))