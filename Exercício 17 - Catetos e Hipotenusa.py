from math import hypot

cop = float(input('Comprimento do cateto oposto: '))
cad = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cop, cad)
print('A hipotenusa é {:.2f}!'.format(hip))
