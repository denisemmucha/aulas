#um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, 
#o salário do comprador e 
# em quantos anos ele vai pagar. 
#A prestação mensal não pode exceder 30% do salário 
#ou então o empréstimo será negado.
print('Olá, vamos analisar seu emprestimo...')
casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = int(input('Em quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
if salario <= minimo:
    print('Emprestimo APROVADO!')
else:
    print('Emprestimo NEGADO!')