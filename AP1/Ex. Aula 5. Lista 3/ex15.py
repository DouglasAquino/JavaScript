cont = 0
massa = float(input('Massa inicial: '))
mf = massa
while mf >= 0.5:
    mf = mf / 2
    cont = cont + 1
tempo = 50 * cont / 3600
print('Massa final: ', massa, 'Hora: ', tempo)
