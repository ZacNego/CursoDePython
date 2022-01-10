lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('-=' * 30)
print(f'Os valores pares em ordem crescente são {lista[0]}')
print(f'Os valores ímpares em ordem crescente são {lista[1]}')
