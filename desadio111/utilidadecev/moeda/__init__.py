def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa/100)
    return res if not formato else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if not formato else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:5>.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=30, taxar=10):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' *40)
    print(f'Preço analizado: \t\t{moeda(preço)}')
    print(f'Dobro do preço: \t\t{dobro(preço, True)}')
    print(f'Metade do preço: \t\t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t\t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preço, taxar, True)}')
    print('-' * 40)
