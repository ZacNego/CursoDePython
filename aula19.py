#pessoas = {'nome':'Isaac', 'sexo':'M','idade':'44' }
'''print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())'''
#pessoas['peso'] = 71
#pessoas['nome'] = 'Mikael'
#for k, v in pessoas.items():
#    print(f'{k} = {v}')
'''brasil = list()
estado1 = {'uf':'Ceará', 'sigla':'CE'}
estado2 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()


