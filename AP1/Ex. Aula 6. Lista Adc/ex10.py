cont = 0
tAlcool = 0
tGasolina = 0
while cont < 100:
    gasolina = float(input('Custo com gasolina: '))
    alcool = float(input('Custo com alcool: '))
    carro = input('U ou P: ')
    print('Gasto com gasolina: ', gasolina * 3.92)
    if gasolina > alcool:
        tGasolina = tGasolina + 1
    if carro == 'p':
        tAlcool = tAlcool + alcool
    cont = cont + 1
print('Carros que usam mais gasolinha: ', tGasolina)
print('Total de litros de alcool com carros de passeio: ', tAlcool)
