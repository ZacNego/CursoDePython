nome = str(input('Qaul é o seu nome? '))
if nome == 'Isaac':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Francisco':
    print('Seu nome é bem popular')
elif nome in 'Ana Claudia Jessica Julianna':
    print("Belo nome feminino")
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))