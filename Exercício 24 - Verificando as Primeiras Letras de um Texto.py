cidade = str(input('Digite o nome de uma cidade: '))
dividido = cidade.upper().split()
print('Começa com SANTO? {}'.format('SANTO' in dividido[0]))
