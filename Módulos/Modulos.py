import math
import random
import emoji
#modulos = bibliotecas
#serve para adicionar funcionalidadess
#import <biblioteca>
#vc pode importar funcionalidades especificas ao inves de toda a biblioteca: from <biblioteca> import funcionalidade
# math traz funcoes matematicas -> ceil arredonda pra cima, floor arredonda para baixo, trunc trunca um numero,
# pow potenciacao, sqrt raiz, factorial fatorial
num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
#mesmo importando a biblioteca eu preciso referenciar o math antes da funcão? simmm

num2 = random.randint(1, 10) #numero aleatorio de 1 a 10

print(num2)
print(emoji.emojize("Olá mundo 🌎"))
