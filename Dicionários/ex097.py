#Faça um programa que leia nome e média de um aluno, guardando também
#a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno ['media']  = float(input('Digite a média do aluno: '))
if aluno['media'] >= 7.00:
    aluno['situacao'] = 'APROVADO'
elif aluno['media'] < 7.00 and aluno['media'] >= 6.00:
    aluno['situacao'] = 'EM RECUPERAÇÃO'
elif aluno['media'] <= 5:
    aluno['situacao'] = 'REPROVADO'
print('+=' * 30)
print(f'NOME: {aluno["nome"]} | MÉDIA: {aluno["media"]} | SITUAÇÃO: {aluno["situacao"]}')
print('+=' * 30)
