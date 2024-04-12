import math

ang = float(input('Forneça o ângulo: '))
rad = math.radians(ang)
print('\nSeno de {:.2f}° = {:.2f}'.format(ang, math.sin(rad)))
print('Cosseno de {:.2f}° = {:.2f}'.format(ang, math.cos(rad)))
print('Tangente de {:.2f}° = {:.2f}'.format(ang, math.tan(rad)))
