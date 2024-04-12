nome = str(input('Digite seu nome completo: '))
dividido = nome.split()
print('Primeiro nome: {}'.format(dividido[0]))
print('Último nome: {}'.format(dividido[len(dividido) - 1]))
