#Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.
#a+b>c
#a+c>b
#b+c>a
cores = {'limpa': '\033[m',
            'azul': '\033[34m',
            'amarelo': '\033[33m',
            'pretoebranco': '\033[7;30m' }
ladoa = float(input('Digite o comprimento do primeiro lado: '))
ladob = float(input('Digite o comprimento do segundo lado: '))
ladoc = float(input('Digite o comprimento do terceiro lado: '))

if ladoa + ladob > ladoc and ladoa + ladoc > ladob and ladob + ladoc > ladoa:
    print('{}Os lados formam um triângulo.{}'.format(cores['azul'], cores['limpa']))
else:
    print('{}Os lados não formam um triângulo.{}'.format(cores['amarelo'], cores['limpa']))