#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
#a) Apenas os 5 primeiros colocados.
#b) Os últimos 4 colocados da tabela.
#c) Uma lista com os times em ordem alfabética.
#d) Em que posição na tabela está o time da Chapecoense.
times = ('Palmeiras', 'Flamengo', 'São Paulo', 'Fluminense', 'Bahia',
         'Athletico-PR', 'Coritiba', 'Atlético-MG', 'Bragantino', 'Vitória',
         'Botafogo', 'Grêmio', 'Vasco da Gama', 'Internacional', 'Santos',
         'Corinthians', 'Cruzeiro', 'Remo', 'Chapecoense', 'Mirassol')
print('Os 5 primeiros colocados são: {}'.format(times[:5]))
print('Os últimos 4 colocados são: {}'.format(times[-4:]))
print('Os times em ordem alfabética são: {}'.format(sorted(times)))
print('O time da Chapecoense está na posição: {}'.format(times.index('Chapecoense') + 1))
