#Crie um programa que leia um número inteiro 
#e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um numero inteiro: '))
if num % 2 == 0: 
    print('Seu numero {} é PAR!'.format(num))
else: 
    print('Seu numero {} é IMPAR!'.format(num))
print('***FIM***')