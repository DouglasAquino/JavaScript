carroA = 14
velA = 120
carroB = 200
velB = 80
cont = 0
while carroA < carroB:
    carroA = carroA + velA
    carroB = carroB + velB
    print(carroA, carroB)
    cont = cont + 1
    if carroA > carroB:
        print('Quantidade de horas que o carro A ultrapassará o carro B: ', cont)
        
