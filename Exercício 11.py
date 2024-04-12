base = float(input('Quantos m de largura? '))
altura = float(input('Quantos m de altura? '))
area = base * altura
print('\nDimensão: {:.2f}m x {:.2f}m\nÁrea da parede = {:.2f}m²'.format(base, altura, area,))
print('Para pintar essa parede, litros de tinta necessários = {:.2f}l'.format(area / 2))
