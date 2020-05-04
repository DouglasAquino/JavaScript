QtMulheres = int(input('Quantidade de Mulheres: '))
QtHomens = int(input('Quantidade de Homens: '))
TotalPessoas = QtMulheres + QtHomens
PcMulheres = QtMulheres / TotalPessoas * 100
PcHomens = QtHomens / TotalPessoas * 100
print('Total de Pessoas: ', TotalPessoas)
print('Percentual de Mulheres: {:.2f}'.format(PcMulheres))
print('Percentual de Homens: {:.2f}'.format(PcHomens))
