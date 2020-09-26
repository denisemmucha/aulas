#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, 
#cobrando R$0,50 por Km para viagens de até 200Km 
#e R$0,45 parta viagens mais longas.
km = float(input('Olá, qual a distancia da sua viajem? '))
if km <=200:
    passagem = 0.50 * km
    print('Sua passagem custará {} reais.'.format(passagem))
else:
    passagem = 0.45 * km
    print('Sua passagem custará {} reais.'.format(passagem))
print('Boa viajem!')