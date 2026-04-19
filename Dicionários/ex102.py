#Aprimore o desafio 099 para que ele funcione com vários jogadores, incluindo 
#um sistema de visualização de detalhes do aproveitamento de cada jogador.
#Crie um programa que gerencia o aproveitamento de um jogador de futebol,
#o programa vai ler o nome do jogador e quantas partidas ele jogou. (for q in quantidadePartidas)
#Depois vai ler a quantidade de gols feitos em cada partida. 
#No final tudo isso será guardado em um dicionário, incluindo o total de gols
#feitos durante o campeonato
from operator import itemgetter

jogador = dict()
jogadores = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['qtd_jogos'] = int(input('Quantidade de jogos: '))
    total_gols = 0
    gols = list()
    for q in range(0, jogador['qtd_jogos']):
        gols.append(int(input('Digite quantos gols foram feitos na partida')))
        total_gols += gols[q]
    jogador['total_gols'] = total_gols
    jogador['gols'] = gols
    jogadores.append(jogador.copy())
    resposta = str(input('Deseja cadastrar mais um jogador? [S/N] ')).upper()
    if resposta != 'S':
        break;
print('-=' * 30)
print('cod ', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end= '')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
      
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca > len(jogadores):
        print(f'ERRO! Não existe jogador com código {busca}')
    else: 
        print(f'LEVANTAMENTO DO JOGADOR: {jogadores[busca]['nome']}')
        for i, v in enumerate(jogadores[busca]['gols']):
            print(f'Na partida {i+1}, fez {v} gols.')
        print(f'Foi um total de {total_gols} gols.')
        
    