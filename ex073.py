#Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valor lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
contador = 0
soma = 0
maior = None
menor = None
resposta = 'S'
while resposta == 'S':
    num = int(input('Digite um número inteiro: '))
    soma += num
    contador += 1
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
    resposta = input('Deseja continuar digitando valores? (S/N): ').upper()

if contador > 0:
    media = soma / contador
    print('A média entre os valores digitados é: {:.2f}'.format(media))
    print('O maior valor digitado foi: {}'.format(maior))
    print('O menor valor digitado foi: {}'.format(menor))