v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('\nMULTADO! Você excedeu o limite de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((v - 80) * 7))
print('\nBoa viagem! Dirija com segurança!')
