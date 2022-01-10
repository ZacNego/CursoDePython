#print(input.__doc__)
#help(input)

'''def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i:início da contagem
    :param f:fim da contagem
    :param p:passo da contagem
    :return:sem retorno
    Função criada por isaac
    """
    c = i
    while c <= f:
        print(f'{c}',end='..')
        c += p
    print('FIM')


contador(0, 100, 10)
help(contador)'''

'''def somar(a=0, b=0, c=0):
    """
    -> Faz a soma dos três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Isaac
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()
help(somar)'''



'''def teste():
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x} ')


#programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()'''

'''def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')


n1 = 2
print(f'N1 fora vale {n1}')
função()'''

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus calculos deram {r1}, {r2} e {r3}')'''

'''def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num =int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')

