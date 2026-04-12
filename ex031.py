n1 = float(input('Digite a primeira nota: '))   
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2 
if m >= 7.0:
    print('Aprovado')
else:
    print('Reprovado')
    
print('Sua média foi {:.1f}'.format(m))