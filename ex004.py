algo = input('Digite algo')

print('tipo de algo: {}'.format(type(algo)))
print('é numerico: {}'.format(algo.isnumeric()))
print('é letra: {}'.format(algo.isalpha()))
print('é alfanumerico: {}'.format(algo.isalnum()))
print('é maiusculo: {}'.format(algo.isupper()))
print('é minusculo: {}'.format(algo.islower()))

#NAO PRECISA DO FORMAT PRA PRINTAR UM BOOLEANO, SÓ CHAMAR O MÉTODO JÁ DA BOM
print('tipo de algo: {}'.format(type(algo)))
print('é numerico:', algo.isnumeric())
print('é letra:', algo.isalpha())
print('é alfanumerico',algo.isalnum())
print('é maiusculo', algo.isupper())
print('é minusculo', algo.islower())
