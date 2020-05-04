SalMim = float(input('Valor do salario mimnimo: '))
funcionario = input('Nome do funcionario: ')
SalTotal = float(input('Salario do funcionario: '))
recebe = SalTotal / SalMim
print('O funcionario: ', funcionario, '\nRecebe {:.2f}'.format(recebe), 'salarios minimos.')
