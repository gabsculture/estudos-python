lanche = ['Hamburger', 'Suco', 'Pizza', 'Pudim']
print(lanche[3])
lanche.append('Cookie') #adiciona o cookie na última posição da lista
lanche.insert(0, 'Cachorro-quente') #adiciona cachorro-quente na posição 0
print(lanche)
print("Apagando usando del\n")
del lanche[3] #apaga elemento na posição 3
print(lanche)
print("Apagando usando pop\n")
lanche.pop() #apaga elemento da última posição
print(lanche)
print("Apagando usando pop(3)")
lanche.pop(3) #apaga elemento na posição 3
print(lanche)
print("Apagando usando remove")
lanche.remove('Suco')
#O del e o pop são ideais para quando queremos apagar usando a posição
#O remove é usado quando queremos apagar usando conteúdo

valores = list(range(4,11))
valores_sem_range = [8,2,5,4,9,3,0]
print(valores_sem_range)
valores_sem_range.sort() #se colocar o reverse = true, ele é ordenado inversamente
print(valores_sem_range)
print(len(valores))

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elemento')

valores_lista = list()
valores_lista.append(5)
valores_lista.append(9)
valores_lista.append(4)
for cont in range(0, 5):
    valores_lista.append(int(input('Digite um número: ')))
    
for c, v in enumerate(valores_lista):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei no final da lista')

a = [2, 3, 4, 7]
b = a# se adicionar [:] após o a, ele cria uma cópia da lista a, então quando for alterada a lista b, a lista a não vai ter alterações também
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#Ao igualar as listas, quando uma alteração ocorre em uma, ela também ocorre na outra

