print('Média abaixo de 5.0 : \033[31;4mREPROVADO\033[m.\nMédia entre 5.0 e 6.9: \033[33;4mRECUPERAÇÃO\033[m.\nMédia 7.0 ou superior: \033[34;4mAPROVADO\033[m.')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua media foi {}.\033[31m REPROVADO\033[m'.format(media))
elif media >= 7:
    print('Sua média foi {}. \033[34mAPROVADO\033[m'.format(media))
elif 7 > media >= 5:
    print('Sua média foi {}. \033[33mRECUPERAÇÃO\033[m'.format(media))


