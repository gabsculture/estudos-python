#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente
resposta = 'S'
valores = list()

while resposta == 'S':
    valor_adicionado = int(input('Adicione um valor: '))
    if valor_adicionado not in valores:
        valores.append(valor_adicionado)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já adicionado. Tente novamente.')
    resposta = str(input('Deseja cadastrar mais um número? [S/N]'))

valores.sort()
print(valores)
    