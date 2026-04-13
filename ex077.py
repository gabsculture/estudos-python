#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
#a) Qual é o total gasto na compra.
#b) Quantos produtos custam mais de
# R$1000.
#c) Qual é o nome do produto mais barato.
total_gasto = 0
contador_produtos_mais_1000 = 0
produto_mais_barato = ''
preco_produto_mais_barato = None
resposta = 'S'

while resposta == 'S':
    nome_produto = input('Digite o nome do produto: ')
    preco_produto = float(input('Digite o preço do produto: R$ '))
    
    total_gasto += preco_produto
    
    if preco_produto > 1000:
        contador_produtos_mais_1000 += 1
    
    if preco_produto_mais_barato is None or preco_produto < preco_produto_mais_barato:
        preco_produto_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    
    resposta = input('Deseja continuar cadastrando produtos? (S/N): ').upper()
print('Total gasto na compra: R$ {:.2f}'.format(total_gasto))
print('Quantidade de produtos que custam mais de R$1000: {}'.format(contador_produtos_mais_1000))
print('O nome do produto mais barato é: {}'.format(produto_mais_barato))