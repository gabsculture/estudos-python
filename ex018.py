import math
#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo, retangulo
#calcule e mostre o comprimento da hipotenusa
catetoOposto = float(input('Digite o cateto oposto '))
catetoAdjacente = float(input('Digite o cateto adjacente '))

hipotenusa = math.sqrt(math.pow(catetoOposto,2) + math.pow(catetoAdjacente,2))
hipotenusaComMath = math.hypot(catetoOposto,catetoAdjacente)

print('cateto oposto: {}, cateto adjacente: {}, hipotenusa: {:.2f}, hipotenusa com math: {:.2f}'.format(catetoOposto, catetoAdjacente, hipotenusa, hipotenusaComMath))
