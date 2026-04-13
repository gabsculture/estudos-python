#for c in range(1, 10):
#print(c, end=' ')
#print('FIM')
#quando eu sei o limite, eu posso usar tanto o for quanto o while,
# mas quando eu não sei o limite, eu só posso usar o while
c = 1
while c < 10:
    print(c, end=' ')
    c += 1  
print('FIM')

n = 1
while n != 0: #Condicao de parada
    n = int(input('Digite um número (0 para parar): '))
print('Programa encerrado.')

r = 'S'
while r == 'S':
    n = int(input('Digite um número: '))
    r = input('Quer continuar? [S/N] ').upper()
print('Programa encerrado.')
