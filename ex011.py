#crie um programa que leia quanto dinheiro tem na carteira e mostre quantos dólares ela pode comprar
dinheiro = float(input('Digite um valor em reais: '))
valorEmDolar = dinheiro/5.13

print('Voce tem {} em reais e pode comprar {} dolares'.format(dinheiro,valorEmDolar))