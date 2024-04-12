nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))  # Alinhamento à direita com 20 chars
print('Prazer em te conhecer, {:=^20}!'.format(nome))  # ====Centralizado==== com 20 chars e "iguais"

print('')
print('')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
divint = n1 // n2
resto = n1 % n2
raiz = n1 ** (1/2)
print('\nSoma = {}\nSubtração = {}\nMultiplicação = {}\nDivisão = {:.3f}'.format(soma, sub, mult, div))
print('A^B = {}\nDivisão inteira = {} e Resto = {}\nRaiz Quadrada de A = {},'.format(pot, divint, resto, raiz), end=' ')
# end -> Não vai pular a linha
print('sendo, A, igual a {}'.format(n1))
