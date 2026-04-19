#Crie um programa que leia nome, ano de nascimento e carteira de trabalho
#e cadastre-os (com idade) em um dicionário se por acaso a CTPS for
#diferente de 0, o dicionário receberá também o ano de contratação e o salário.
#calcule e acrescente, além da idade, com quantos anos a pessoa vai se 
#aposentar
from datetime import date
pessoa = dict()
pessoa['nome'] = str(input("Digite o nome da pessoa: "))
ano_Nascimento = int(input("Digite o ano de nascimento da pessoa: YYYY"))
anoAtual =  date.today().year
idade = anoAtual - ano_Nascimento
pessoa['idade'] = idade
pessoa['ctps'] = int(input("Digite o número da CTPS: "))
pessoa['sexo'] = str(input("Digite o sexo da pessoa:"))
if pessoa['ctps'] != 0:
    pessoa['ano_contratacao'] = int(input("Qual o ano de contratação?"))
    pessoa['salario'] = float(input('Qual o seu salário?'))
    if pessoa['sexo'] == 'F':
        tempo_minimo = 15
        anos_contribuicao = anoAtual - pessoa['ano_contratacao']
        anos_faltam = tempo_minimo - anos_contribuicao
        if tempo_minimo <= anos_contribuicao:
            pessoa['idade_Aposentadoria'] = idade
        else:
            idade_Aposentadoria = pessoa['idade'] + anos_faltam
            pessoa['idade_Aposentadoria'] = idade_Aposentadoria
    elif pessoa['sexo'] == 'M':
        tempo_minimo = 20
        anos_contribuicao = anoAtual - pessoa['ano_contratacao']
        anos_faltam = tempo_minimo - anos_contribuicao
        if tempo_minimo <= anos_contribuicao:
            pessoa['idade_Aposentadoria'] = idade
        else:
            idade_Aposentadoria = pessoa['idade'] + anos_faltam
            pessoa['idade_Aposentadoria'] = idade_Aposentadoria
    print(f'NOME: {pessoa['nome']} | IDADE: {pessoa["idade"]} | SEXO: {pessoa["sexo"]} | CTPS: {pessoa["ctps"]} | ANO CONTRATAÇÃO: {pessoa["ano_contratacao"]} | SALARIO: {pessoa["salario"]} | IDADE QUE VAI APOSENTAR: {pessoa["idade_Aposentadoria"]}')
else:
    print(f'NOME: {pessoa['nome']} | IDADE: {pessoa["idade"]} | SEXO: {pessoa["sexo"]}')
