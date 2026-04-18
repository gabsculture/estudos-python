#Crie um programa que tenha uma tuplica única com nomes de produtos e seus respectivos preços na sequencia
# Depois disso, mostre uma listagem de preços organizando os dados em forma tabular.
produtos = ('Arroz', 10.50, 'Feijão', 8.30, 'Macarrão', 5.20, 'Óleo', 7.00)
print('LISTAGEM DE PREÇOS')
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:.<20} R${produtos[i+1]:.2f}')
    