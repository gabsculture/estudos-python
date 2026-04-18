#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
# a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

kmPercorridos = float(input('qual a quantidade de km percorridos? '))
diasAlugados = int(input('qual a quantidade de dias alugados? '))
precoKm = kmPercorridos*0.15
precoDiaria = diasAlugados*60
precoTotal = precoKm+precoDiaria

print('A quantidade de km percorridos foi {} e preco {}'.format(kmPercorridos, precoKm))
print('A quantidade de dias alugados foi {} e preco {}'.format(diasAlugados, precoDiaria))
print('O preco total foi de {}'.format(precoTotal))

