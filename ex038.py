#Escreva um programa que pergunte o salário de um funcionario e calculoo o valor do seu aumento
#Para salaários superiores a R$1.250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.
cores = {'limpa': '\033[m',
            'azul': '\033[34m',
            'amarelo': '\033[33m',
            'pretoebranco': '\033[7;30m' }

salario = float(input('Digite o salário do funcionário: R$'))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
novo_salario = salario + aumento
print('O novo salário do funcionário é {}R${:.2f}{}.'.format(cores['azul'], novo_salario, cores['limpa']))