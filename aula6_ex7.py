#Escreva um programa que pergunte o salário de um funcionário
#e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, 
# calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual seu salario atual? '))
if salario > 1250:
    aumento = salario * 1.10
    print('Seu salario com 10% de aumento será: {:.2f}.'.format(aumento))
else:
    aumento = salario * 1.15
    print('Seu salario com 15% de aumento será: {:.2f}.'.format(aumento))