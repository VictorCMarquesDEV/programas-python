r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))
if r3 < (r1 + r2) and r2 < (r1 + r3) and r1 < (r2 + r3):
    print('Pode formar um triângulo!')
else:
    print('Não pode formar triângulo!')
