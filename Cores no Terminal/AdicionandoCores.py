#Sempre que você quiser representar um cor no python é necessário iniciar com o código
#\033[m e finalizar com o código \033[m. Entre esses códigos, você pode colocar o código da cor que deseja usar.
#\033[estilo texto fundo m
#\033[0;33;44m
#Códigos de estilo:
# 0 - None Sem estilo nenhum
# 1 - Bold Negrito
# 4 - Underline Sublinhado  
# 7 - Negative Inverte as cores
# Códigos de texto:
# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul
# 35 - Roxo
# 36 - Ciano
# 37 - Cinza
# Códigos de fundo:
# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul
# 45 - Roxo
# 46 - Ciano
# 47 - Cinza
#preto
#Para usar mais cores é necessário usar a biblioteca colorama, que é uma biblioteca de terceiros 
# que permite usar cores no terminal de forma mais fácil e compatível com diferentes sistemas operacionais.
#Para instalar a biblioteca colorama, basta usar o comando pip install colorama no terminal.

print('\033[1;30;41m Teste \033[m')
print('\033[4;33;44m Teste \033[m')
print('\033[0;35;43m Teste \033[m')
print('\033[1;30;42m Teste \033[m')
print('\033[m Teste \033[m')
print('\033[7;30m  Teste \033[m')