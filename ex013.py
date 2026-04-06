#algoritmo que le o preõ de um produto e calcula o novo preço com 5% de desconto
preco = float(input('digite o valor do preco'))
desconto = preco*0.05
novoPreco = preco - desconto
print('o preco inicial é {}, o desconto de 5% é {}, logo o novo preço é {}'.format(preco, desconto, novoPreco))