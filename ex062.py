#Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.
from datetime import date

ano_atual = date.today().year
maioridade = 0
menoridade = 0
for i in range(1, 8):
    ano_nascimento = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        maioridade += 1
    elif idade < 21:
        menoridade += 1

print('Pessoas que ainda não atingiram a maioridade: {}'.format(menoridade))
print('Pessoas que já atingiram a maioridade: {}'.format(maioridade))