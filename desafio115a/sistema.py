from desafio115a.lib.interface import *
from desafio115a.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        # Opção cadastrar conteudo no arquivo
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Sair do aruivo
        cabeçalho('Saindo do Sistema... até logo! ')
        break
    else:
        cabeçalho('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
