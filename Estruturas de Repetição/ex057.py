#algoritmo que le um numero inteiro e mostra na tela a tabuada
numero = int(input('digite um valor'))
print('A tabuada do número {} é;'.format(numero))
for i in range(1, 11):
    print('{} X {} = {}'.format(i, numero, i * numero))
