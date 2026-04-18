lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
#Tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas.
#lanche[1] = 'Refrigerante' #Isso causará um erro, pois não é possível modificar um elemento de uma tupla.

print(lanche[1]) #acessando o elemento na posição 1 (Suco)]
print(lanche[0]) #acessando o elemento na posição 0 (Hambúrguer)
print(lanche[2]) #acessando o elemento na posição 2 (Pizza)
print(lanche[-1]) #acessando o último elemento da tupla (Pudim)
print(lanche[-2]) #acessando o penúltimo elemento da tupla (Pizza)
print(lanche[1:3]) #acessando os elementos da posição 1 até
# a posição 2 (Suco e Pizza)
print(lanche[2:]) #acessando os elementos a partir da posição 2 (Pizza e Pudim)
print(lanche[:2]) #acessando os elementos até a posição 1 (Hambúrguer e Suco)
print(lanche[-2:]) #acessando os últimos 2 elementos da tupla
print(len(lanche)) #mostrando a quantidade de elementos da tupla
print(sorted(lanche)) #mostrando os elementos da tupla em ordem alfabética

for comida in lanche:
    print(f'Eu vou comer {comida}') #interpolação de string (f-string) - disponível a partir do Python 3.6
print('Comi pra caramba!')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #interpolação de string (f-string) - disponível a partir do Python 3.6

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}') #interpolação de string (f-string) - disponível a partir do Python 3.6

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #concatenando as tuplas a e b, a ordem influencia no resultado da concatenação, 
#ou seja, a tupla a será concatenada antes da tupla b
print(c) #mostrando a tupla resultante da concatenação
print(c.count(5)) #mostrando a quantidade de vezes que o número 5 aparece na tupla c
print(c.index(8)) #mostrando a posição do número 8 na tupla c
print(c.index(2)) #mostrando a posição do número 2 na tupla c, o resultado será a posição do primeiro número 2 encontrado na tupla c
print(c.index(2, 4)) #mostrando a posição do número 2 na tupla c, a partir da posição 4, o resultado será a posição do segundo número 2 encontrado na tupla c

pessoa = ('Gustavo', 39, 'M', 99.88, 'São Paulo')
del(pessoa) #deletando a tupla pessoa, isso é possível porque a tupla é imutável, ou seja, não pode ser alterada depois de criada, mas pode ser deletada
print(pessoa) #mostrando a tupla pessoa