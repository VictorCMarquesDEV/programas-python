dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Kms percorridos? '))
custo = (dias * 60) + (km * 0.15)
print('Preço a pagar: R${:.2f}'.format(custo))
