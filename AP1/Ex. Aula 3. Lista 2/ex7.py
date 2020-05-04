A = float(input('Lado A: '))
B = float(input('Lado B: '))
C = float(input('Lado C: '))
if A < B+C and B < A+C and C < A+B:
    print('É um triangulo!')
    if A==B and B==C:
        print('Equilatero!')
    elif A==B or B==C or A==C:
        print('Isosceles!')
    else:
        print('Escaleno!')
else:
    print('Não pódem ser medidas de um triangulo: ')
