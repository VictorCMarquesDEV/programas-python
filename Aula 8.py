# import math -> importa toda a biblioteca
# from math import sqrt -> importa apenas o sqrt

from math import sqrt, ceil, floor
import random
import emoji

num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é {:.2f}!'.format(num, raiz))
print('A raiz de {} é {}!'.format(num, ceil(raiz)))  # ceil -> arredonda pra cima
print('A raiz de {} é {}!'.format(num, floor(raiz)))  # floor -> arredonda pra baixo

num = random.randint(1, 10)
print(num)

print(emoji.emojize('Olá, mundo! :globe_showing_Americas:'))
