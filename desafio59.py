from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opção = 0
while opção!= 5:
    print('''    [ 1 ] soma
    [ 2 ] multiplicação
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print('A soma {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente!')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção Invalida. Tente novamente!')
    print('=-='*10)
    sleep(2)
print('Fim do programa. Volte sempre!')
