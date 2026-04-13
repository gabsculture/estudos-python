#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Python', 'Programação', 'Exercício', 'Vogais')
for palavra in palavras:
    vogais = ()
    for letra in palavra.lower():
        if letra in 'aeiou' and letra not in vogais:
            vogais += (letra,)
    print(f'\nNa palavra {palavra} temos as vogais: ', end='')
    for v in vogais:
        print(v, end=' ')
