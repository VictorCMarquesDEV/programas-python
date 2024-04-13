import random
import time
num = random.randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print('-=-' * 20)

palpite = int(input('Em que número eu pensei? '))
print('-=-' * 20)
time.sleep(3)

if palpite < 0 or palpite > 5:
    print('\nIntervalo inválido! Jogo encerrado!')
    exit(0)
else:
    if palpite == num:
        print('\nPARABÉNS! Você me venceu!\nO número sorteado foi {}!'.format(palpite))
    else:
        print('\nGANHEI!\nEu pensei no {} e não no {}.'.format(num, palpite))
