#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúscukas
#Quantas letras ao todo, sem considerar os espaços
#Quantas letras tem o primeiro nome

nome = str(input("digite seu nome completo: "))#posso fazer o strip aqui direto

print(nome.upper())
print(nome.lower())
primeiroNome = nome.split()[0]
segundoNome = nome.split()[1]
print(len(primeiroNome.strip() + segundoNome.strip()))
print(len(primeiroNome))