n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}\nO produto é {}\nA divisão e {:.2f}'.format(s,m,d), end='>>>')
print('Divisão inteira {}\nPotência {}'.format(di,e))
