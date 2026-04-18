dados = list()
dados.append('Pedro')
dados.append(25)
dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)
print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:])
print(pessoas)
pessoas_declaradas = [['Pedro',25], ['Maria', 19], ['João', 32]]
print(pessoas_declaradas[0][0])
print(pessoas_declaradas[1][1])
print(pessoas_declaradas[2][0])
print(pessoas_declaradas[1])

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera_declarada = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera_declarada)
print(galera_declarada[0][0])
print(galera_declarada[2][1])
for p in galera_declarada:
    print(p[0])

for p in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
    
totmai = 0
totmen = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
        
print(f'Temos {totmai} maiores e {totmen} menores de idade')