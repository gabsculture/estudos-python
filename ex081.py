#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor 
# que estão na tupla.
import random
numeros = tuple(random.randint(0, 100) for _ in range(5))
print('Números gerados:', numeros)
print('O menor número é:', min(numeros))
print('O maior número é:', max(numeros))

