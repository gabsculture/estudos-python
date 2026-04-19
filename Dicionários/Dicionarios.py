#diciionarios são declarados com {}
dados = dict()
dados = {'nome': 'Pedro', 'idade':25}
print(dados['nome'])
print(dados['idade'])
dados['sexo'] = 'M'
del dados['idade']
filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')
    
locadora = list()
locadora.append(filme)
print(locadora[0]['ano'])

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
    
for v in pessoas.values():
    print(v)
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
for k,v in pessoas.items():
    print(f'{k} é {v}')
    
brasil = []
estado1 = {'UF': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
estado = dict()
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['sigla'])
print(brasil[0]['UF'])

for c in range(0, 3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}.')
        
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()