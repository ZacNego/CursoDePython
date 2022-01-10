from time import sleep
n = int(input('Digite um numero: '))
print('Bomba Acionada')
for c in range(n, -1, -1):
    print(c)
    sleep(.5)
print('BUMMMMMMMMMM')