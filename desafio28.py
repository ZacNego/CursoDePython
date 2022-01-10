from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pense? '))#o jogador tenta adivinhar
print('processando...')
sleep(3)
if jogador == computador:
    print('Parabens, você conseguiu me vencer ')
else:
    print('Ganhei,eu pensei no número {} e não no {}'.format(computador, jogador))



