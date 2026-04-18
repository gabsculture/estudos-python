#algoritmo que le o salario de um funcionario e mostra seu novo salario com 15% de aumento
salario = float(input('digite seu salario'))
aumento = salario*0.15
salarioNovo = salario+aumento

print('seu salario é {}, sua porcentagem de aumento é {}, e seu salario com o aumento é {}'.format(salario, aumento, salarioNovo))
