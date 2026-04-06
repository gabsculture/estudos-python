# adição +, subtração -, multiplicação *, divisão /
# ** potência, // divisao inteira, % resto da divisao
soma = 5 + 2
subtracao = 5 -2
multiplicacao = 5 * 2
divisao = 5 / 2
potencia = 5**2
divisaoInteira = 5//2
resto = 5%2

print('soma entre 5 e 2 {}'.format(soma))
print('subtracao entre 5 e 2 {}'.format(subtracao))
print('multiplicacao entre 5 e 2 {}'.format(multiplicacao), end=' ') #tira a quebra de linha, dentro '' pode ser adicionado qualquer caractere
print('divisao entre 5 e 2 {:.3f}'.format(divisao)) #adiciona 3 casas decimais
print('potencia entre 5 e 2 {}'.format(potencia))
print('divisao inteira entre 5 e 2 {}'.format(divisaoInteira))
print('resto entre 5 e 2 {}'.format(resto))

#ORDEM DE PRECEDENCIA
#1 parenteses
#2 potenciacao
#3 multiplicacao, divisao, divisao inteira
#4 subtraçao, soma
