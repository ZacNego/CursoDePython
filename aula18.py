'''teste = list()
teste.append('Isaac')
teste.append(44)
galera = list()
galera.append(teste[:])
teste[0] = 'maria'
teste[1] = 24
galera.append(teste[:])
print(galera)'''

#galera = [['Isaac', 44], ['Valéria', 40], ['Thayna', 14], ['Mikael', 5]]
#print(galera[2][1])
#for p in galera:
 #   print(f'{p[0]} tem {p[1]} anos de Idade.')

galera = list()
dados = list()
totmai = totmen = 0
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

