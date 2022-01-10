def fatorial(n, show=False):
    """
    -> calcula a fatorial de um numero:
    :param n: numero a ser calulado.
    :param show:(opcional) mostrar ou não a conta.
    :retorno: O valor da Fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f

#programa principal
n = int(input('Digite um número: '))
x = str(input('Quer mostra os calculos? [S/N] ')).upper()[0]
if 'N' in x:
    x = False
else:
    x = True
print(fatorial(n, show=x))
