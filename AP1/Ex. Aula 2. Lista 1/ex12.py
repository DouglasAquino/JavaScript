UnidadesVendidas = float(input('Quantidade vendida: '))
PrecoUnidade = float(input('Preço da unidade: '))
PrecoVenda = float(input('Preço de venda Unitária: '))
arrecadado = UnidadesVendidas * (PrecoVenda - PrecoUnidade)
lucro = arrecadado - 500
print('O lucro foi: ', lucro)
