velocidade1 = 80
distancia1 = 240
prog1 = 0

velocidade2 = 90
distancia2 = 450
prog2 = 0

velocidade3 = 70
distancia3 = 280
prog3 = 0

while distancia1 > 0:
    distancia1 = distancia1 - velocidade1
    prog1 = prog1 + 1
while distancia2 > 0:
    distancia2 = distancia2 - velocidade2
    prog2 = prog2 + 1
while distancia3 > 0:
    distancia3 = distancia3 - velocidade3
    prog3 = prog3 + 1
if prog1 < prog2 and prog1 < prog3:
    print('O carro que chegará primeiro é o 1!')
if prog2 < prog1 and prog2 < prog3:
    print('O carro que chegará primeiro é o 2!')
if prog3 < prog1 and prog3 < prog2:
    print('O carro que chegará primeiro é o 3!')
