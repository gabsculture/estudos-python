#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
#com valores inteiros
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior
def maior(* valores):
    maior_valor = None
    for valor in valores:
        if maior_valor == None or valor >= maior_valor:
            maior_valor = valor
    
    print(f'O maior valor da lista é: {maior_valor}')
    
maior(1, 2, 3, 4, 5, 6, 9, 7)