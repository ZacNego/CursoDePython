import moeda
p = float(input('Digite um valor: R$ '))
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'Aumentando 10% é R${moeda.aumentar(p, 10)}')
print(f'Diminuindo 10% é R${moeda.diminuir(p, 10)}')