#um programa que leia um nome completo
#mostre com todas letras maiusculas
#mostre com todas as letras minusculas
#quantas letras tem ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome
nc = str(input('Olá, qual seu nome completo? ')).strip()
#strip para cortar os espaços inuteis antes e depois do nome
print('Vamos ao resultado do seu nome...')
print('O nome em upper é {}'.format(nc.upper()))
print('O nome em lower é {}'.format(nc.lower()))
print('O seu nome tem {} letras'.format(len(nc) - nc.count(' ')))
#len para contar e - count espaço para diminuir os espaços entre o nome
print('Seu primeiro nome tem {} letras'.format(nc.find(' ')))
#como o python conta de 0 a ... ele irá dar o resultado correto ao contar ate o espaço.