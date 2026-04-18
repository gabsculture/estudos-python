#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
numeros = list()
for cont in range (0, 7):
    numeros.append(int(input('Digite um número:')))

numeros_pares = list()
numeros_impares = list()
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
        
print(f"Números pares: {numeros_pares}")
print(f"Números ímpares: {numeros_impares}")