#Faça um programa que leia um numero qualquer e mostre o seu fatorial
num = int(input('Digite um número para calcular seu fatorial: '))
while num < 0:
    print('Número inválido. Digite um número não negativo.')
    num = int(input('Digite um número para calcular seu fatorial: '))

fatorial = 1
contador= 0
while contador < num: #enquanto o contador for menor que o numero
    fatorial *= (num - contador) # o fatorial é multiplicado pelo numero menos o contador (ex: fatorial *= (5 - 0) -> fatorial *= 5, depois fatorial *= (5 - 1) -> fatorial *= 4, e assim por diante)
    contador += 1 #aumenta o contador
print('O fatorial é: {}'.format(fatorial))