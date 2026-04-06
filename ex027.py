#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input('Digite seu nome completo: ')).upper()
bool = 'SILVA' in nome
print(bool)