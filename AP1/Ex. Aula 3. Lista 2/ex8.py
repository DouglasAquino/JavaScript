produto = float(input('Valor do produto: '))
pagamento = float(input('Valor do pagamento: '))
troco = pagamento - produto
if pagamento < produto:
    print('Valor Insuficiente!', '\nFalta: ', produto - pagamento)
elif pagamento == produto:
    print('Valor exato! Não tem troco.')
else:
    print('Valor superior, tem troco de R${:.2f}'.format(troco))
