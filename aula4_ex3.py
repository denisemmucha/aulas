#um programa que leia um angulo qualquer
#mostre o valor do seno, cosseno e tangente desse angulo
import math
num = float(input('Digite o angulo: '))
seno = math.sin(math.radians(num))
cosseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print('O seno do angulo {} é {:.2f}.\nO cosseno é {:.2f}.\nE a tangente {:.2f}.'.format(num, seno, cosseno, tangente))