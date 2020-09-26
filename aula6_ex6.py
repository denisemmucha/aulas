#Faça um programa que leia três números
#e mostre qual é o maior e qual é o menor.
num1 = int(input('Olá, digite um numero: '))
num2 = int(input('Digite outro numeero: '))
num3 = int(input('E mais um: '))
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O menor numero digitado foi: {}'.format(menor))
print('O maior numero digitado foi: {}'.format(maior))
print('***FIM***')