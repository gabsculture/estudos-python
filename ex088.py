#Crie um programa que vai ler vários números e colocar em uma lista
#Depois disso,  mostre:
#a) Quantos números foram digitados.
#b) A lista de valores ordenada de forma decrescente
#c) Se o valor 5 foi digitado e está ou não na lista

lista = list()
resposta = 'S'

while resposta == 'S':
    lista.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja adicionar mais um valor? [S/N] ')).upper()
    if resposta == 'N':
        break
    
print(f'A quantidade de números digitados foi: {len(lista)}')
lista.sort(reverse=True)
print(lista)
for valor in lista:
    if 5 in lista:
        has_5 = True
    else:
        has_5 = False

if has_5:
    print('O 5 foi digitado e está na lista.')
else: 
    print('O 5 não foi digitado e não está na lista')