
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = simp = mai = scol1 = scol2 = scol3 = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        else:
            simp += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores impares é {simp}')
for l in range(0, 3):
    scol1 += matriz[l][0]
    scol2 += matriz[l][1]
    scol3 += matriz[l][2]
print(f'A soma da primeida coluna é {scol1}')
print(f'A soma da segunda coluna é {scol2}')
print(f'A soma da terceira coluna é {scol3}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior elemanto da segunda linha é {mai} ')
