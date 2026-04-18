#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
#No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista
valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor numérico: ')))
    
menor_valor = None
maior_valor = None
posicao_maior = None
posicao_menor = None

for cont in range(0, 5):
    if maior_valor is None or valores[cont] > maior_valor:
        maior_valor = valores[cont]
        posicao_maior = cont
    if menor_valor is None or valores[cont] < menor_valor:
        menor_valor = valores[cont]
        posicao_menor = cont
print(f'O maior valor é: {maior_valor} e está na posição {posicao_maior}')
print(f'O menor valor é: {menor_valor} e está na posição {posicao_menor}')            