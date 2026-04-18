#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
if ano_nascimento > ano_atual:
    print('Ano de nascimento inválido. Por favor, digite um ano válido.')
    ano_nascimento = int(input('Digite o ano de nascimento: '))

idade = ano_atual - ano_nascimento
if idade <= 9:
    print('O atleta tem {} anos. Categoria: MIRIM'.format(idade))
elif idade <= 14 and idade > 9:
    print('O atleta tem {} anos. Categoria: INFANTIL'.format(idade))
elif idade <= 19 and idade > 14:
    print('O atleta tem {} anos. Categoria: JÚNIOR'.format(idade))
elif idade <= 25 and idade > 19:
    print('O atleta tem {} anos. Categoria: SÊNIOR'.format(idade))
elif idade > 25:
    print('O atleta tem {} anos. Categoria: MASTER'.format(idade))
