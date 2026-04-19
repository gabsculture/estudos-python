#Faça um programa que tenha uma função chamada escreva(), que receba um texto como
#parâmetro e mostre uma mensagem com tamanho adaptável

def escreva(txt):
    adaptacao = len(txt)
    print('-' * adaptacao)
    print(txt)
    print('-' * adaptacao)
escreva('Olá mundo!')