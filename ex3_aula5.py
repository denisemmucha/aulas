#programa que leia o nome de uma cidade
#e diga se ela começa com 'santo' ou nao
cidade = str(input('Diga o nome de uma cidade: ')).strip()
#sempre usar o strip para cortar espaços inuteis
print(cidade[:5].upper() == 'SANTO')
#usar o upp para que caso o usuario digite com letras maiusculas/minusculas nao de erro