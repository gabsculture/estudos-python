#Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.
numero = 0;

while numero >= 0:
    print('Digite um número para ver sua tabuada (negativo para sair): ')
    numero = int(input())
    if numero >= 0:
        print('Tabuada de {}:'.format(numero))
        for i in range(1, 11):
            print('{} x {} = {}'.format(numero, i, numero * i))
print('Programa encerrado. Obrigado por usar a tabuada!')
