#Faça um programa que leia trÊs números e mostre qual é o maior e qual é o menor.
cores = {'limpa': '\033[m',
            'azul': '\033[34m',
            'amarelo': '\033[33m',
            'pretoebranco': '\033[7;30m' }

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2            
else:
    menor = num3
    
print('O maior número é {}{}{} e o menor número é {}{}{}.'.format(cores['azul'], maior, cores['limpa'], cores['amarelo'], menor, cores['limpa']))