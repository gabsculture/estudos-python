#Refaça o desafio dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

ladoa = float(input('Digite o comprimento do primeiro lado: '))
ladob = float(input('Digite o comprimento do segundo lado: '))
ladoc = float(input('Digite o comprimento do terceiro lado: '))

if ladoa + ladob > ladoc and ladoa + ladoc > ladob and ladob + ladoc > ladoa:
    print('Os lados formam um triângulo.')
    if ladoa == ladob == ladoc:
        print('O triângulo é EQUILÁTERO.')
    elif ladoa == ladob and ladoa != ladoc and ladob != ladoc:
        print('O triângulo é ISÓSCELES.')
    elif ladoa == ladoc and ladoa != ladob and ladob != ladoc:
        print('O triângulo é ISÓSCELES.')
    elif ladob == ladoc and ladob != ladoa and ladoa != ladoc:
        print('O triângulo é ISÓSCELES.')
    else:
        print('O triângulo é ESCALENO.')
else:
    print('Os lados não formam um triângulo.')