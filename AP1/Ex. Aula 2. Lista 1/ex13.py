ValorHoraTrabalhada = float(input('Valor da Hora Trabalhada: '))
QtHoraTrabalhada = float(input('Quantidade de Hora Trabalhada: '))
TaxaImposto = float(input('Taxa de Imposto: '))
SalBruto = ValorHoraTrabalhada * QtHoraTrabalhada * 4.5
ValorDesconto = SalBruto * TaxaImposto / 100
SalLiquido = SalBruto - ValorDesconto
print('Salario Bruto: ', SalBruto)
print('Valor do Desconto: ', ValorDesconto)
print('Salario Liquido: ', SalLiquido)
