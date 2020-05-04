CustoFabrica = float(input('Custo de Fabrica: '))
PrecoDespachante = CustoFabrica * 28 / 100
impostos = CustoFabrica * 45 / 100
soma = CustoFabrica + PrecoDespachante + impostos
print('Preço do Carro: ', 'R$', soma)
