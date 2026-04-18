#Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
#- À vista dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto
#- Em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros
preco = float(input('Digite o preço do produto: R$'))
print('Escolha a forma de pagamento:')
print('1 - À vista dinheiro/cheque')
print('2 - À vista no cartão')
print('3 - Em até 2x no cartão')
print('4 - 3x ou mais no cartão')
opcao = int(input('Digite a opção de pagamento (1, 2, 3 ou 4): '))
if opcao == 1:
    valor_final = preco * 0.90
    print('O valor a ser pago é R${:.2f} com 10% de desconto.'.format(valor_final))
elif opcao == 2:
    valor_final = preco * 0.95
    print('O valor a ser pago é R${:.2f} com 5% de desconto.'.format(valor_final))
elif opcao == 3:
    valor_final = preco
    print('O valor a ser pago é R${:.2f} sem desconto.'.format(valor_final))
elif opcao == 4:
    valor_final = preco * 1.20
    print('O valor a ser pago é R${:.2f} com 20% de juros.'.format(valor_final))
else:
    print('Opção inválida. Por favor, escolha uma opção entre 1 e 4.')