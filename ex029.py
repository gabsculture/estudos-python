#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
#ex: ana maria de souza
#primeiro = ana
#ultimo souza

nome = str(input('Digite seu nome completo: '))
qtdNomes = len(nome.split())
primeiroNome = nome.split()[0]
ultimoNome = nome.split()[qtdNomes -1]
print('primeiro nome: {}'.format(primeiroNome))
print('ultimo nome: {}'.format(ultimoNome))
