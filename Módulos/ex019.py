import math
#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
#e tangente desse ângulo
angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Angulo: {} Seno: {:.2f} Cosseno: {:.2f} Tangente: {:.2f}'.format(angulo, seno, cosseno, tangente))