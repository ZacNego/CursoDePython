número = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADÉCIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(número, bin(número)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(número, oct(número)[2:]))
elif opção == 3:
    print('{} convertido para HEXADÉCIMAL é igual a {}'.format(número, hex(número)[2:]))
else:
    print('OPIÇÃO INVÁLIDA, TENTE NOVAMENTE')
