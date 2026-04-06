#algoritmo que le a largura e a altura de uma parede em metros, calcula area e a quantidade de litros de tinta
largura = int(input('Qual a largura da parede?'))
altura = int(input('Qual a altura da parede?'))

area = largura*altura
quantidadeTinta = area/2

print('A area de uma parede com  {} m de largura e {} m de altura é {}, e a quantidade de litros de tinta necessárias para pintar são {}'.format(largura, altura, area, quantidadeTinta))