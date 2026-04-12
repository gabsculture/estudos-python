#condições aninhadas sintaxe:
# if condição 1:
#    bloco1
# elif condição 2:
#    bloco2
# elif condição 3:
#    bloco3
# else:
#    bloco4
#o else eh opcional
nome = str(input('Digite seu nome: ')).capitalize()
if nome == 'Gabriela':
    print('que nome lindo!')
elif nome == 'Maria' or nome == 'Ana' or nome == 'João':
    print('que nome popular!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('que nome feminino!')
else:
    print('que nome comum!')
print('Tenha um bom dia, {}!'.format(nome))