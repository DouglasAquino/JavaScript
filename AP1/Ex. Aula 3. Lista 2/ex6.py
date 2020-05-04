Distancia = float(input('Digite o valor da Distancia: '))
QtLitros = float(input('Quantidade de litros: '))
consumo = Distancia / QtLitros
if consumo < 1:
    print('Consumo impossivel!')
elif consumo <= 9:
    print('Venda o carro!')
elif consumo <= 14:
    print('Economico!')
else:
    print('Ual!, não venda o carro!')
    
