precoKWH = float(input('Preço do Kwh: '))
numCons = int(input('Numero do consumidor: '))
menorCon = 999999
contres = 0
somaCon = 0
contCon = 0
while numCons != 0:
    qtKWH = float(input('Quantidade de KWH: '))
    tipo = input('Tipo: ')
    totalPagar = precoKWH * qtKWH
    print('O consumidor {}, pagará R${}.'.format(numCons, totalPagar))
    if menorCon > qtKWH:
        menorCon = qtKWH
    if tipo == 'residencial' and qtKWH < 100:
        contres = contres + 1
    somaCon = somaCon + qtKWH
    contCon = contCon + 1
    numCons = int(input('Numero do consumidor: '))
print('Menor consumo: ', menorCon)
print('Quantidade de consumidores de residencia que usaram menos que 100KWH: ', contres)
print('Media de consumo: ', somaCon / contres)
