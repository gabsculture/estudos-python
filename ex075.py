#Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
vitorias = 0
while True:
    escolha = input('Par ou Ímpar? [P/I] ').upper()
    jogador = int(input('Digite um número: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = 'par' if total % 2 == 0 else 'impar'
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} - {tipo}')
    if (escolha == 'P' and tipo == 'par') or (escolha == 'I' and tipo == 'impar'):
        print('Você venceu!')
        vitorias += 1
    else:
        print('Você perdeu!')
        break
print(f'Game Over! Você venceu {vitorias} vezes consecutivas.')