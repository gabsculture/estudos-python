#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
linha_1 = list()
linha_2 = list()
linha_3 = list()

coluna_1 = list()
coluna_2 = list()
coluna_3 = list()

for cont in range(0,3):
    linha_1.append(int(input('Digite os valores da primeira linha: ')))

for cont in range(0,3):
    linha_2.append(int(input('Digite os valores da segunda linha: ')))

for cont in range(0,3):
    linha_3.append(int(input('Digite os valores da terceira linha: ')))
    
coluna_1.append(linha_1[0])
coluna_2.append(linha_2[0])
coluna_3.append(linha_3[0])

coluna_1.append(linha_1[1])
coluna_2.append(linha_2[1])
coluna_3.append(linha_3[1])

coluna_1.append(linha_1[2])
coluna_2.append(linha_2[2])
coluna_3.append(linha_3[2])

linhas = list()
linhas.append(linha_1)
linhas.append(linha_2)
linhas.append(linha_3)

for linha in linhas:
    print(linha)
    
#JEITO OTIMIZADO:
matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
for l in  range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]'))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
    print()