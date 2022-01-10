from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''OPÇÕES DE JOGO
[ 0 ] - PEDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA''')
while True:
    jogador = int(input('Qual é a sua jogada? '))
    while jogador < 0 or jogador > 2:
        jogador = int(input("Digite novamente!!!: "))
    print('JO')
    sleep(.5)
    print('KEN')
    sleep(.5)
    print('PÔ!!!')
    sleep(.5)
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('JOGADOR VENCE')
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('Fim de jogo')