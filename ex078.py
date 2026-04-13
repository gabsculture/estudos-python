#Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor_saque = int(input('Digite o valor a ser sacado: R$ '))
cedulas_50 = valor_saque // 50
valor_saque = valor_saque % 50
cedulas_20 = valor_saque // 20
valor_saque = valor_saque % 20
cedulas_10 = valor_saque // 10
valor_saque = valor_saque % 10
cedulas_1 = valor_saque // 1
print('Cédulas de R$50: {}'.format(cedulas_50))
print('Cédulas de R$20: {}'.format(cedulas_20))
print('Cédulas de R$10: {}'.format(cedulas_10))
print('Cédulas de R$1: {}'.format(cedulas_1))
