s = float(input('Qual é o seu salário? '))
if s > 1250:
    print('Seu novo salário será de R${:.2f}'.format(s * 1.1))
else:
    print('Seu novo salário será de R${:.2f}'.format(s * 1.15))
