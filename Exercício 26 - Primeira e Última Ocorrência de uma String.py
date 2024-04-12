frase = str(input('Digite uma frase: ')).strip().upper()
print('Número de letras A: {}'.format(frase.count('A')))
print('Aparece primeiro em: {}'.format(frase.find('A') + 1))
print('Aparece por último em: {}'.format(frase.rfind('A') + 1))
