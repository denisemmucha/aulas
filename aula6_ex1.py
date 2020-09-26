#Escreva um programa que faça o computador "pensar" em um número inteiro 
#entre 0 e 5 e peça para o usuário tentar descobrir 
#qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
print('Vou pensar em um numero e voce tenta adivinhar...')
num = random.randint(0, 5)
#usar randint para gerar numero inteiro
resposta = int(input('Em que numero eu pensei? '))
print('Carregando...')
if resposta == num:
    print('Parabens! Eu pensei no numero {}. VOCE GANHOU!'.format(num))
else:
    print('PERDEU! Eu pensei no numero {} e não no {}.'.format(num, resposta))
print('--FIM--')