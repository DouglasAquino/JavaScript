nascidas = int(input('Quantidade de crianças nascidas: '))
sexo = input('Sexo: ')
cMortas = 0
menor = 0
masc = 0
while sexo == 'm' or sexo == 'f':
    meses = int(input('Quantidade de meses: '))
    if meses < 12:
        menor = menor + 1
    elif sexo == 'm' and meses >= 12:
        masc = masc + 1
    cMortas = cMortas + 1
    sexo = input('Sexo: ')
print('Percentual de crianças mortas: ', cMortas * 100 / nascidas)
print('Mortos menores que 1 ano: ', menor)
print('Masculinos mortos maiores que 12 meses: ', masc)
