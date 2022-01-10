numero = int(input("\033[2;34mMe diga um número qualquer:\033[m "))
resultado = numero % 2
if resultado == 0:
    print('\033[1;31mO número {} é PAR\033[m'.format(numero))
else:
    print('\033[2;35mO número {} é IMPAR\033[m'.format(numero))
