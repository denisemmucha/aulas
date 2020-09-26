#Faça um programa que leia uma frase pelo teclado 
#e mostre quantas vezes aparece a letra "A", 
#em que posição ela aparece a primeira vez 
#e em que posição ela aparece a última vez.
frase = str(input('Escreva uma frese qualquer: ')).upper().strip()
print('A letra A apareceu {} vezes na frase'.format(frase.count('A')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('Ultima posição foi {}'.format(frase.rfind('A')+1))
#adicionar o +1 para que a contagem se adequade.