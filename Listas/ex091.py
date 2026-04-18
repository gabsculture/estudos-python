#Faça umm programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista.
#No final mostre:
#a) Quantas pessoas foram cadastradas
#b) Uma listagem com as pessoas mais pesadas.
#c) Uma listagem com as pessoas mais leves.

pessoas = list()
pessoa = list()
pessoas_leves = list()
pessoas_pesadas = list()
resposta = 'S'
total = 0
while resposta == 'S':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()
    total += 1
    resposta = str(input('Deseja registrar mais uma pessoa? [S/N]'))


peso_mais_leve = None
for p in pessoas:
    if peso_mais_leve == None or p[1] < peso_mais_leve:
        peso_mais_leve = p[1]
    if p[1] == peso_mais_leve:
        pessoas_leves.append(p)
        
peso_mais_pesado = None
for p in pessoas:
    if peso_mais_pesado == None or p[1] > peso_mais_pesado:
        peso_mais_pesado = p[1]
    if p[1] == peso_mais_pesado:
        pessoas_pesadas.append(p)

print(f'{total} pessoas foram cadastradas.')
print(f'{peso_mais_pesado} maior peso')
print(f'{peso_mais_leve} menor peso')
print(f'Pessoas mais pesadas: {pessoas_pesadas} com o peso: {peso_mais_pesado}')
print(f'Pessoas mais leves: {pessoas_leves} com o peso: {peso_mais_leve}')