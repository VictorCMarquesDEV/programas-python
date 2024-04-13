menor = n1 = int(input('Forneça um número: '))
n2 = int(input('Forneça outro número: '))
maior = n3 = int(input('Forneça mais um número: '))
if n2 > n3:
    menor1 = n3
else:
    menor1 = n2
print('O menor é {}'.format(menor) if menor < menor1 else 'O menor é {}'.format(menor1))

if n1 > n2:
    maior1 = n1
else:
    maior1 = n2
print('O maior é {}'.format(maior) if maior > maior1 else 'O maior é {}'.format(maior1))
