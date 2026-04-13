n = s = 0
while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n == 999:
        break
    s += n
print('A soma dos números digitados é: {}'.format(s))
print(f'A soma dos números digitados é: {s}') #interpolação de string (f-string) - disponível a partir do Python 3.6