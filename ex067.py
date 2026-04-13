#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
opcao = int(input('Escolha uma opção:\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa\n'))
while opcao != 5:
    if opcao == 1:
        print('A soma entre {} e {} é: {}'.format(n1, n2, n1 + n2))
        break
    elif opcao == 2:
        print('A multiplicação entre {} e {} é: {}'.format(n1, n2, n1 * n2))
        break
    elif opcao == 3:
        if n1 > n2:
            print('O maior número entre {} e {} é: {}'.format(n1, n2, n1))
            break
        elif n2 > n1:
            print('O maior número entre {} e {} é: {}'.format(n1, n2, n2))
            break
        else:
            print('Os números são iguais.')
            break
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        break
    
