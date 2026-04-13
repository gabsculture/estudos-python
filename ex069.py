#Refaça o desafio da PA, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são:')
contador = 0
while contador < 10:
    termo = primeiro_termo + contador * razao
    print(termo, end=' ')
    contador += 1
