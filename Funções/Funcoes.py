def mostraLinha():
    print('-' * 30)

def mensagem(msg):
    print(msg)
mostraLinha()
mensagem('        Curso em Vídeo  ')
mostraLinha()

def soma(a, b):
    soma = a + b
    print(soma)
a = 4
b = 5
soma(a, b)

def contador(*num): #transforma em tuplas os parâmetros
    print(num) 
    tam = len(num) #vc consegue trabalhar com todas as funções de tuplas

def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1
    
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def somar(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
    

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
