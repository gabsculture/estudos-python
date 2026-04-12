#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
numero = random.randint(0, 5)
print('Pensei em um número entre 0 e 5. Tente adivinhar...')
chute = int(input('Qual número eu pensei?'))

if chute == numero:
    print('Parabéns! Você acertou!')
else:    
    print('Que pena! Você errou. O número era {}.'.format(numero))