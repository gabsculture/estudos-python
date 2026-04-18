#Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ')
frase_sem_espacos = frase.replace(' ', '').lower()
for i in range(len(frase_sem_espacos) // 2):
    if frase_sem_espacos[i] != frase_sem_espacos[-(i + 1)]:
        print('A frase não é um palíndromo.')
        break
    else:
        print('A frase é um palíndromo.')
        break;