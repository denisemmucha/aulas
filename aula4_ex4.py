#sortear entre 4 nomes um para auxiliar o professor
#ler o nome deles e escrever o do escolhido
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
lista = [a1, a2, a3, a4]
#qualquer lista no python deve ser usada dentro de []
print('Agora que temos nossa lista, vamos sortear!')
print('O aluno sorteado foi {}.'.format(random.choice(lista)))