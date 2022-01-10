pessoas = []
dados = []
maiorp = menorp = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorp  = menorp = dados[1]
    else:
        if dados[1] > maiorp:
            maiorp = dados[1]
        if dados[1] < menorp:
            menorp = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {maiorp}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorp:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menorp}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorp:
        print(f'[{p[0]}] ', end='')
print()