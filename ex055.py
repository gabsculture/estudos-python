#Crie um programa que mostra na tela todos os números pares que estão no intervalo entre 1 e 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')
