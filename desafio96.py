def area(a, b):
    s = a * b
    print(f'A area de um terreno {a}X{b} é de {s}m2.')

#programa principal
print(' Controle de Terreno')
print('-=' * 30)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)