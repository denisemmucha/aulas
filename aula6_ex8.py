#Desenvolva um programa que leia o comprimento de três retas 
#e diga ao usuário se elas podem ou não formar um triângulo.
print('Olá, vamos formar um triangulo!')
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seus três segmentos formam um triangulo!')
else:
    print('Infelizmente não foi possivel formar um triangulo!')
print('FIM!!')