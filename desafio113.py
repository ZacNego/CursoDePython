def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! por favor digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n


n1 = leiaint('Digite um Inteiro: ')
n2 = leiafloat('Digite um Real: ')
print(f'O valor Inteiro foi {n1} e o real {n2}')
