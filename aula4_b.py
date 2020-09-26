#programa que leia um numero real e mostre sua porçao inteira
import math
num = float(input('Digite um numero com virgula: '))
print('A porção inteira do seu numero é {}.'.format(math.ceil(num)))