# n1 = input('Digite um valor: ') -> Dessa forma, causaria erro pois str(n1) != int(n2)
n1 = int(input('Digite um valor: '))
print(type(n1))
n2 = int(input('Digite outro valor: '))
print(type(n2))
s = n1 + n2
print('A soma entre {} e {} = {}!'.format(n1, n2, s))  # Print mais simples

print('')
print('')

valor = bool(input('Digite um valor: '))  #Se colocar valor = True, se não colocar valor = False
print(valor)

print('')
print('')

n = input('Digite algo: ')
print(n.isnumeric())  # Vai dizer se é possível converter a str para número
print(n.isalpha())  # Vai dizer se é possível converter a str para letra
print(n.isalnum())  # Vai dizer se é possível converter a str para letra-número
