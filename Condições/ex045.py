#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal.
numeroInteiro = int(input('Digite um número inteiro: '))
print('Escolha a base de conversão:')
escolha = int(input('1 para binário, 2 para octal e 3 para hexadecimal: '))
if escolha == 1:
    print('O número {} convertido para BINÁRIO é: b{}'.format(numeroInteiro, bin(numeroInteiro)[2:]))
elif escolha == 2:
    print('O número {} convertido para OCTAL é: o{}'.format(numeroInteiro, oct(numeroInteiro)[2:]))
elif escolha == 3:
    print('O número {} convertido para HEXADECIMAL é: 0x{}'.format(numeroInteiro, hex(numeroInteiro)[2:]))
    