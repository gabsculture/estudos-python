#Crie um programa que gerencia o aproveitamento de um jogador de futebol,
#o programa vai ler o nome do jogador e quantas partidas ele jogou. (for q in quantidadePartidas)
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final tudo isso será guardado em um dicionário, incluindo o total de gols
#feitos durante o campeonato
from operator import itemgetter

jogador = dict()
nome = str(input('Nome do jogador: '))
qtd_jogos = int(input('Quantidade de jogos: '))
total_gols = 0
gols = list()
for q in range(0, qtd_jogos):
    gols.append(int(input('Digite quantos gols foram feitos na partida')))
    total_gols += gols[q]

jogador['nome'] = nome
jogador['qtd_jogos'] = qtd_jogos
jogador['gols'] = gols
jogador['total_gols'] = total_gols
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

for i, v in enumerate(gols):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {total_gols} gols.')