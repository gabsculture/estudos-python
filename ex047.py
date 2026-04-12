#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
if ano_nascimento > ano_atual:
    print('Ano de nascimento inválido. Por favor, digite um ano válido.')
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    
idade = ano_atual - ano_nascimento
if idade < 18:
    print('Você tem {} anos. Ainda faltam {} anos para o alistamento.'.format(idade, 18 - idade))
elif idade == 18:
    print('Você tem {} anos. Está na hora de se alistar!'.format(idade))
elif idade > 18:
    print('Você tem {} anos. Já passou do tempo de alistamento em {} anos.'.format(idade, idade - 18))