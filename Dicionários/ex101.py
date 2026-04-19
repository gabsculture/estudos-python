#Crie um programa que leia nome, sexo, idade de veárias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários
#em uma lista.
#No final mostre:
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo
#C) Uma lista com todas as mulheres.
#D) Uma lista com todas as pessoas com idade acima da média

pessoa = dict()
pessoas = list()
somaIdades = 0
mulheres = list()
acima_media = list()

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome da pessoa: '))
    pessoa['sexo'] = str(input('Digite o sexo da pessoa [F/M]:'))
    pessoa['idade'] = int(input('Digite a idade da pessoa: '))
    somaIdades += pessoa['idade']
    pessoas.append(pessoa.copy())
    resposta = str(input('Deseja cadastrar outra pessoa? [S/N] ')).upper()
    if resposta != 'S':
        break

mediaIdade = somaIdades/len(pessoas)
for p in pessoas:
        if p['idade'] > mediaIdade:
            acima_media.append(p)
        if p['sexo'] == 'f' or p['sexo'] == 'F':
            mulheres.append(p)
            
print(f'O grupo de pessoas é: {pessoas}')
print(f'A quantidade de pessoas é: {len(pessoas)}')
print(f'A média de idade do grupo é: {mediaIdade}')
print(f'As mulheres do grupo são: {mulheres}')
print(f'As pessoas com idade acima da média são: {acima_media}')


    