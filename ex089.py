#Crie um programa que vai ler vários números e colocar me uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares 
# e os valores ímpares digitados respectivamente.
#Ao final mostre o conteúdo gerado das 3 listas

resposta = 'S'
valores = list()
pares = list()
impares = list()

while resposta == 'S':
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja adicionar mais um valor? [S/N] ')).upper()

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'Lista original: {valores}')
print(f'Lista dos pares: {pares}')
print(f'Lista dos ímpares: {impares}')

    