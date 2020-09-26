#um programa que leia um valor em reais e converta em dolar
n = int(input('Olá, diga um valor: '))
d = n / 5.39
print('Você tem hoje, em dolares, o valor de: ${:.2f}'.format(d))