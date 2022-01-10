print('{:=^40}'.format(' CONDIÇÕES DE PAGAMENTO '))
preço = float(input('Valor do produto: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] A VISTA - DINHEIRO/CHEQUE: 10% DE DESCONTO
[ 2 ] A VISTA - CARTÃO: 5% DE DESCONTO
[ 3 ] 2 X - CARTÃO: PREÇO NORMAL
[ 4 ] 3 X OU MAIS - CARTÃO: 20% DE JUROS''')
opção = int(input('Qual a opção? '))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço * 1.20
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))


