from datetime import date
ano = int(input('Digite um ano para analisar, para analisar o ano atual coloque 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano \033[0;34m{}\033[m é \033[4;31mBISSEXTO\033[m'.format(ano))
else:
    print('O ano \033[0;34m{}\033[m não é \033[4;31mBISSEXTO\033[m'.format(ano))
