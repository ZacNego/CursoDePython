'''def lin():
    print('-' * 30)

# program principal
lin()
print('CURSO EM VIDEO')
lin()
print('APRENDA PYTHON')
lin()
print('ISAAC LAUREANO')
lin()'''

'''def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

# program principal
titulo('CURSO EM VIDEO')
titulo('APRENDA PYTHON')
titulo('ISAAC LAUREANO')'''

'''def soma(a, b):
    print(f'A = {a} e B = {b} ')
    s = a + b
    print(f'A soma A + B = {s}.')

#programa principal
soma(b=4, a=5)
soma(b=7, a=2)'''

'''def contador(*núm):
    #for v in núm:
     #   print(f'{v}  ', end='')
    #print('FIM!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todos {tam} números. ')
contador(2, 1, 7)
contador(8, 8)
contador(4, 4, 7, 6, 2)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 4, 3, 2, 7]
dobra(valores)
print(valores)'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(1, 2, 3, 4, 5, 6, 7, 8, 9)
