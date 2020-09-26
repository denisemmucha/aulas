#um programa  que sorteie a ordem de apresentação de 4 alunos
import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
alunos = [a1, a2, a3, a4]
random.shuffle(alunos)
#usamos o shuffle para embaralhar
print('Agora que temos nossa lista de alunos, vamos sortear!')
print(alunos)