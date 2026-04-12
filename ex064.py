#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa mostre:
#a) A média de idade do grupo
#b) Qual é o nome do homem mais velho
#c) Quantas mulheres têm menos de 20 anos
soma_idade = 0
mulheres_menos_20 = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
for i in range(1, 5):
    nome = input('Digite o nome da {}ª pessoa: '.format(i))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    sexo = input('Digite o sexo da {}ª pessoa (M/F): '.format(i)).upper()
    soma_idade += idade
    if sexo == 'M':
        if i == 1:
            homem_mais_velho = nome
            idade_homem_mais_velho = idade
        else:
            if idade > idade_homem_mais_velho:
                idade_homem_mais_velho = idade
                homem_mais_velho = nome

    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1
    
media_idade = soma_idade / 4
print('A média de idade do grupo é: {:.1f}'.format(media_idade))
print('O nome do homem mais velho é: {}'.format(homem_mais_velho))
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(mulheres_menos_20))
