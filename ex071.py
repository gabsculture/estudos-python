#Escreva um programa que leia um número inteiro qualquer
#e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#F(n)=F(n−1)+F(n−2)

n = int(input('Digite um número inteiro para mostrar os n primeiros elementos da Sequência de Fibonacci: '))
primeiros_elementos = []
a , b = 0, 1
while len(primeiros_elementos) < n:
    primeiros_elementos.append(a)
    a, b = b, a + b
print('Os {} primeiros elementos da Sequência de Fibonacci são: {}'.format(n, primeiros_elementos))
