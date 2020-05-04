SalMim = float(input('Salario minimo: '))
QtWatts = float(input('KiloWatts gastos: '))
gasto = (SalMim / 100) * QtWatts
print('Valor a ser pago {:.2f}. '.format(gasto))
