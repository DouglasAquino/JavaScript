cont = 0
media = 0
while cont < 5:
    PrecoCompra = float(input('Preço de compra: '))
    PrecoVenda = float(input('Preço de venda: '))
    lucro = PrecoVenda - PrecoCompra
    print('Lucro R$', lucro)
    media = media + lucro
    cont = cont + 1
print('Média R$', media / 5)
