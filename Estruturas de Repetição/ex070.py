#Melhore o desafio 069, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerra quando ele disser que quer mostrar 0 termos.


primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Os 10 primeiros termos da PA são:')

contador = 0
ultimo_termo = primeiro_termo

while contador < 10:
    termo = primeiro_termo + contador * razao
    print(termo, end=' ')
    ultimo_termo = termo
    contador += 1

resposta = input('\nQuer mostrar mais termos? [S/N] ').upper()
if resposta == 'S':
    while resposta == 'S':
        quantidade_termos = int(input('Quantos termos você quer mostrar? '))
        contador = 0
        while contador < quantidade_termos and quantidade_termos != 0:
            ultimo_termo += razao
            print(ultimo_termo, end=' ')
            contador += 1
        resposta = input('\nQuer mostrar mais termos? [S/N] ').upper()

