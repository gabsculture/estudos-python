import math
#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua proção inteira
#MINHA SOLUÇÃO
#numReal = float(input('Digite um valor real: '))
#inteiro = math.floor(numReal)
#print('O valor digitado é {} e o inteiro {}'.format(numReal, inteiro))

#FORMA CORRETA DE FAZER
num = float(input('Digite um valor real: '))
print('O valor digitado foi {} e o inteiro {}'.format(num, math.trunc(num)))