#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separados
#exemplo: digite 1834 unidade = 4, dezena = 3, centena = 8, milhar = 1

numero = int(input('Digite um numero'))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000  % 10
print('Milhar: {}'.format(milhar))
print('Centena: {}'.format(centena))
print('Dezena: {}'.format(dezena))
print('Unidade: {}'.format(unidade))