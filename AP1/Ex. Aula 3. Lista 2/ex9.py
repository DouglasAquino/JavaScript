preco = float(input('Valor do produto: '))
forma = input('Forma de pagamento: ')
if forma == 'a vista no dinheiro' or forma == 'a vista no cartao de debito':
    print('Valor a pagar com desconto: ', preco - preco * 0.10)
elif forma == 'a vista no cartao de credito':
    print('Valor a pagar com desconto: ', preco - preco * 0.05)
elif forma == 'parcelado em duas vezes':
    print('Valor Total: ', preco, '\nValor das parcelas: {:.2f} '.format(preco/2))
else:
    parc = preco + preco
    if forma == 'parcelado em tres vezes':
        print('Valor Total: ', parc, 'Valor das parcelas: {:.2f}'.format(parc/3))
