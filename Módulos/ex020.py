import random
#um professor quer sortear um dos seus quatro alunos para apagar o quadro
#faça um programa que ajude ele, lendo o nome deles e escrevendo o escolhido
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]

numSorteio = random.choice(lista)
print('O aluno sorteado foi o {}'.format(numSorteio))