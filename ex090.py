#Crie um programa onde o usuário digite uma expressão qualquer com parênteses. Seu aplicativo deverá
#analisar se a expressão passada está com o parêntes abertos e fechados na ordem correta.
expressao = input('Digite a expressão: ')

pilha = []
valido = True

for char in expressao:
    if char == '(':
        pilha.append(char)
    elif char == ')':
        if len(pilha) == 0:
            valido = False
            break
        pilha.pop()

if len(pilha) == 0 and valido:
    print('Sua expressão é válida')
else:
    print('Sua expressão está errada!')