#crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada
numero = int(input('digite um numero: '))

dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2) # pow(numero, (1/2))

print('O numero digitado foi {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(numero, dobro, triplo, raiz))