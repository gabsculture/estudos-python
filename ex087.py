#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os na lista,
#já na posição correta de inserção (sem usar o sort()).
#No final mostre a lista ordenada na tela.
valores = list()
for cont in range(0, 5):
    valor_digitado = int(input('Insira um valor: '))
    if len(valores) == 0:
        valores.append(valor_digitado)
    else:
        i = 0
        while i < len(valores) and valores[i] < valor_digitado:
            i +=1
        
        valores.insert(i, valor_digitado)
print(valores)