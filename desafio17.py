import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = math.hypot(co, ca)
print('Hipotenusa é igua a: {:.2f}.'.format(hip))

