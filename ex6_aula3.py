#ler o preço de um produto com 5% de desconto
produto = int(input('Diga o valor do seu produto: '))
desconto = (produto * 5) / 100
resultado = produto - desconto
print('O valor da sua peça com desconto de 5% é: {}'.format(resultado))