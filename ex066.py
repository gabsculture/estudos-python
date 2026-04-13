#Melhore o jogo do desafio 032 onde o computador vai pensar em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites 
# foram necessários para vencer.
import random
numero = random.randint(0, 10)
print('Pensei em um número entre 0 e 10. Tente adivinhar...')
chute = int(input('Qual número eu pensei?'))
palpites = 1

while chute != numero:
    print('Que pena! Você errou. Tente novamente.')
    chute = int(input('Qual número eu pensei?'))
    palpites += 1
print('Parabéns! Você acertou com {} palpites!'.format(palpites))