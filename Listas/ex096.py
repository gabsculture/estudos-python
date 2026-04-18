#Crie um programa que leia o nome e duas notas de vários alunos,
#e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um 
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
n = 1
print(n**2 if n > 6 else n for n in range(10) if n % 2 == 0)
aluno = list()
alunos = list()
while True:
    aluno.append(str(input("Digite o nome do aluno: ")))
    aluno.append(float(input("Digite a nota 1 do aluno: ")))
    aluno.append(float(input("Digite a nota 2 do aluno: ")))
    media = ((aluno[1] + aluno[2])/2)
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    resposta = str(input("Deseja cadastar mais um aluno? [S/N]")).upper()
    if resposta == 'N':
        break

print("-=" * 30)

for aluno in alunos:
    print(f'NOME: {aluno[0]} | NOTA 1: {aluno[1]} | NOTA 2: {aluno[2]} | NOTA FINAL: {aluno[3]}')
    

