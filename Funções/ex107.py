#Faça um programa que tenha uma lista chamada números e duas funções chamadas
#Sorteio() e somaPar(). A primeira função vai sortear 5 números e vai colocá-las
#Dentro da lista e a segunda função vai mostrar a soma entre todos os valores
#PARES sorteados pela função anterior
import random
def Sorteio(lista):
    for c in range(0, 5):
        n = random.randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
    print()

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Soma dos pares: {soma}')

numeros = list()
Sorteio(numeros)
somaPar(numeros)
