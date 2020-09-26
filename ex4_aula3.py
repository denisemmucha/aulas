#calcular a area de uma parede 
# e quantidade necessaria de tinta p pinta-la
#cada litro pinta uma area de 2m cubicos
l = int(input('Digite a largura de sua parede em metros: '))
a = int(input('Agora a altura: '))
area = l * a
tinta = area / 2 
print('Você possui uma area de {} m2 e precisará de {} litros de tinta.'.format(area, tinta))