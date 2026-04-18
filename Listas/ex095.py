#Faça um programa que ajude um jogador da mega sena a criar palpites. 
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta.
import random
jogo = list()
jogos = list()
quantidadeJogos = int(input("Quantos jogos você deseja jogar?"))
numero = 0
while numero != quantidadeJogos:
    for c in range (0, 6):
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    numero += 1

print(jogos)