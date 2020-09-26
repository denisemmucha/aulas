#uso do if, elif, e else.
nome =  str(input('Olá, qual seu nome? '))
if nome == 'Denise':
    print('Que nome bonito!')
elif nome == 'Robson':
    print('Que nome lindo você tem!')
#posso usar or se quiser mais de uma opção de nome dentro do elif ou if.
else:
    print('Que nome normal...')
print('Tenha um bom dia, {}.'.format(nome))