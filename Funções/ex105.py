#Faça um programa que tenha uma função chamada contador(),
#que receba três parâmetros: início, fim e passo d realize a contagem
#seu programa tem que realizar três contagens através da função criada
#a) De 1 até 10, de 1 em 1
#b) De 10 até 0, de 2 em 2
#c) Uma contagem personalizada
def contador(inicio, fim, passo):
    print(f'Indo de {inicio} até {fim} de {passo} em {passo}')
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont += passo
    else:
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont -= passo
    print('Fim')


    

contador(1, 10, 1)
contador(10, 1, 2)
inicio = int(input('Digite o valor de início'))
fim = int(input('Digite o valor de fim'))
passo = int(input('Digite o valor do passo'))
contador(inicio, fim, passo)
