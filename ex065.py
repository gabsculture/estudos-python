#Faça um programa que leia o sexo de uma pessoa,
#mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = input('Digite o sexo da pessoa (M/F): ').upper()
while sexo != 'M' and sexo != 'F':
    print('Valor inválido. Digite novamente.')
    sexo = input('Digite o sexo da pessoa (M/F): ').upper()
print('Sexo {} registrado com sucesso.'.format(sexo))