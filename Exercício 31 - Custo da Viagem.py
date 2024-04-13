d = float(input('Qual a distância da viagem? '))
print('O preço da passagem será de ', end='')
print('R${:.2f}'.format(d * 0.50) if d <= 200 else 'R${:.2f}'.format(d * 0.45))
