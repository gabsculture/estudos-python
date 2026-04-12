#Cre um porgrama que leia um número inteiro e mostre na tela se ele é par ou ímpar.
n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print('O número {} é par.'.format(n))
else: 
    print('O número {} é ímpar.'.format(n))
    