from random import randint
computador = randint(0, 10) #faz o computador pensar
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegui adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))#o jogador tenta adivinhar
    palpites += 1
    if jogador == computador:
        acertou = True
    else:     #ajudando o jogador
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Párabens!'.format(palpites))


