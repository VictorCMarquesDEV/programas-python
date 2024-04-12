tempo = int(input('Quantos anos têm seu carro? '))
if tempo <= 3:
    print('Seu carro está novo!')
else:
    print('Seu carro está velho!')

print('Seu carro está novo!' if tempo <= 3 else 'Seu carro está velho!')  # Forma secundária para if mais simples

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A sua média foi: {:.2f}!'.format(media))
if media < 6:
    print('Sua média foi ruim! ESTUDE MAIS!')
else:
    print('Sua média foi boa! Parabéns!')

print('Parabéns!' if media >= 6 else 'Estude mais!')
