a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# verificando quem pe o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[;36mO menor valor digitado foi \033[4;31m{}\033[m'.format(menor))
print('\033[36mO maior valor digitado foi \033[4;31m{}\033[m'.format(maior))
