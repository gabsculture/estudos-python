#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#a) Quantas pessoas tem mais de 18 anos.
#b) Quantos homens foram cadastrados.
#c) Quantas mulheres tem menos de 20 anos.
resposta = 'S'
contador_maiores_18 = 0
contador_homens = 0
contador_mulheres_menos_20 = 0

while resposta == 'S':
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa (M/F): ').upper()
    
    if idade > 18:
        contador_maiores_18 += 1
    if sexo == 'M':
        contador_homens += 1
    if sexo == 'F' and idade < 20:
        contador_mulheres_menos_20 += 1
    
    resposta = input('Deseja continuar cadastrando pessoas? (S/N): ').upper()
    
print('Quantidade de pessoas com mais de 18 anos: {}'.format(contador_maiores_18))
print('Quantidade de homens cadastrados: {}'.format(contador_homens))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(contador_mulheres_menos_20))