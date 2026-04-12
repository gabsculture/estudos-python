#Crie um programa que faça o computador jogar Jokenpô com você.
import random
print('Vamos jogar Jokenpô!')
itens = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0, 2)
print('Suas opções:')
print('0 - Pedra')
print('1 - Papel')
print('2 - Tesoura')
jogador = int(input('Qual é a sua jogada? '))
print('O computador jogou {}'.format(itens[computador]))
if jogador == computador:
    print('Empate!')
    print('Vamos jogar novamente!')
elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
    print('Parabéns, você venceu!')
elif (jogador == 0 and computador == 1) or (jogador == 1 and computador == 2) or (jogador == 2 and computador == 0):
    print('Que pena, você perdeu!')