times = ('Atlético-MG', 'Palmeiras', 'Fortaleza','Flamengo','Bragantino',
         'Corinthians', 'Internacional', 'Fluminense', 'Athletico-PR',
         'Cuiabá', 'Ceará', 'Atlético-GO', 'São Paulo', 'Juventude',
         'América-MG', 'Santos', 'Bahia', 'Grêmio', 'Sport Recife',
         'Chapecoense')
print('-='* 15)
print(f'Lista de Times {times}')
print('-='* 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='* 15)
print(f'Os 4 Ultimos são {times[-4:]}')
print('-='* 15)
print(f'Times em ordem alfabetica {sorted(times)}')
print('-='* 15)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')


#for t in times:
 #   print(t)