# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima  do limite.

velocidade = float(input("Qual é a velocidade de carro?"))
if velocidade > 80:
    multa = (velocidade - 80) * 7;
    print("Você foi multado no valor de R$ {:.2f}!".format(multa))
else:
    print("Tenha um bom dia! Dirija com segurança!")