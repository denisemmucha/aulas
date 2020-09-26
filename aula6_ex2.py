#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre mensagem que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite
velocidade = float(input('A que velocidade voce estava? '))
if velocidade > 80: 
    multa = (velocidade - 80) * 7
    print('Você foi multado em {} reais! Dirija com mais cuidado!'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança')
print('***FIM***')