#Aprimore o desafio anterior, mostrando no final:
#a) A soma de todos os valores pares digitados.
#b) a soma dos valores da terceira coluna
#c) o maior valor da segunda linha.
#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

''''linha_1 = list()
linha_2 = list()
linha_3 = list()

coluna_1 = list()
coluna_2 = list()
coluna_3 = list()
soma_pares = 0
soma_terceira_coluna = 0
soma_segunda_linha = 0

for cont in range(0,3):
    linha_1.append(int(input('Digite os valores da primeira linha: ')))
    if linha_1[cont] / 2 == 0:
        soma_pares += linha_1[cont]   

for cont in range(0,3):
    linha_2.append(int(input('Digite os valores da segunda linha: ')))
    if linha_2[cont] / 2 == 0:
        soma_pares += linha_2[cont]

for cont in range(0,3):
    linha_3.append(int(input('Digite os valores da terceira linha: ')))
    if linha_3[cont] / 2 == 0:
        soma_pares += linha_3[cont]

maior_valor = None
for valor in linha_2:
    if maior_valor == None or maior_valor < valor:
        maior_valor = valor
    
coluna_1.append(linha_1[0])
coluna_2.append(linha_2[0])
coluna_3.append(linha_3[0])

coluna_1.append(linha_1[1])
coluna_2.append(linha_2[1])
coluna_3.append(linha_3[1])

coluna_1.append(linha_1[2])
coluna_2.append(linha_2[2])
coluna_3.append(linha_3[2])

i = 0
for i in coluna_3:
    soma_terceira_coluna += coluna_3[i]
    i +=1


linhas = list()
linhas.append(linha_1)
linhas.append(linha_2)
linhas.append(linha_3)
print(f'Soma de todos os valores pares digitados: {soma_pares}')
print(f'Soma de todos os valores da terceira coluna: {soma_terceira_coluna}')
print(f'Maior valor da segunda linha: {maior_valor}')
print(linhas)
'''

#JEITO OTIMIZADO
matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
soma = 0
soma_terceiro = 0
maior_valor_segunda_linha = 0

for l in  range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))
print('-=' * 30)

for l in range(0, 3):       
    soma_terceiro += matriz[l][2]
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if l == 1:
            if maior_valor_segunda_linha == 0 or matriz[1][c] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[1][c]
    print()
    
print(f'Soma de todos os valores pares digitados: {soma}')
print(f'Soma de todos os valores da terceira coluna: {soma_terceiro}')
print(f'Maior valor da segunda linha: {maior_valor_segunda_linha}')