print('\033[2;34m-=-\033[m'*10)
print('\033[7;34mAnalisador de Triângulos\033[m')
print('\033[2;34m-=-\033[m'*10)
l1 = float(input('\033[34mPrimeiro segmento:\033[m '))
l2 = float(input('\033[34mSegundo segmento:\033[m '))
l3 = float(input('\033[34mTerceiroo segmento:\033[m '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('\033[34mOs segmentos acima \033[7mPODEM FORMAR TRIÂNGULO\033[m\033[34m!')
else:
    print('\033[31mOs segmentos acima \033[7mNÃO PODEM FORMAR TRIÂNGULO\033[m\033[31m!')
