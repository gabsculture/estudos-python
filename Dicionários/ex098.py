#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo 
#que o vencedor tirou o maior número no dado
#o jogo vai gerar valores de 0 a 6
#Wos jogadores não podem repetir valores
import random
import time
from operator import itemgetter
jogo = {
    'jogador1': random.randint(1, 6),
    'jogador2': random.randint(1, 6),
    'jogador3': random.randint(1, 6),
    'jogador4': random.randint(1, 6)
}
ranking = dict()

print('Valores sorteados:')
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    time.sleep(1)