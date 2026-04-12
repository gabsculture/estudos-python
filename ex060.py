#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
import math
num = int(input('Digite um número inteiro: '))
if num < 2:
    print('O número {} não é primo.'.format(num))
else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print('O número {} é primo.'.format(num))
    else:
        print('O número {} não é primo.'.format(num))
        