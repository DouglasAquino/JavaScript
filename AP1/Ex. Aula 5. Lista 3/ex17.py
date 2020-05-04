velMax = float(input('Velocidade maxima permitida: '))
nao = 0
maiorMulta = 0
cont = 0
totalM = 0
velCarro = float(input('Velocidade do carro: '))
while velCarro != 0:
    if velCarro <= velMax:
        nao = nao + 1
        print('Motorista está dentro da velocidade permitida!')
    else:
        print('Motorista está acima da velocidade permitida!')
        multa = (velCarro - velMax) * 10.00
        print('Valor da multa: ', multa)
        if multa > maiorMulta:
            maiorMulta = multa
        totalM = totalM + multa
    velCarro = float(input('Velocidade do carro: '))
    cont = cont + 1

print('Porcentagen de carros que NAO foram multados: ', nao * 100 / cont)
print('Maior Multa: ', maiorMulta)
print('Valor arrecadado: ', totalM)
