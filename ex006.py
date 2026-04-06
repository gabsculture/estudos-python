#faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
numero = int(input('Digite um numero'))

antecessor = numero - 1
sucessor = numero + 1

print ('O antecessor e sucesssor do numero {} são, respectivamente, {} e {}'.format(numero, antecessor, sucessor))