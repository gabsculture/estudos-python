
for i in range(1, 6):
    print('Oi')
print('Fim')

for c in range(0, 3): #c = contador
    print(c) #vai imprimir o valor de c, que começa em 0 e vai até 2, pois o 3 é exclusivo
print('Fim')

for c in range(0, 7, 2): #c = contador, o 2 é o passo, ou seja, vai pular de 2 em 2
    print(c)
print('Fim')

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)   
print('Fim')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)    
print('Fim')

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n #s = s + n 
print('O somatório de todos os valores é {}'.format(s))


