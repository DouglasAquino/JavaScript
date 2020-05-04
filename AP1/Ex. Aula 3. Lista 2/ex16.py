creditos = int(input('Quantidade de créditos: '))
atrasos = int(input('Dias atrasados: '))
valor = 80 * creditos
print('Valor da mensalidade R$', valor)
if atrasos == 0:
    print('Pagamento em dia, pagará o valor da mensalidade!')
else:
    if atrasos > 0:
        print('Pagamento em atraso!')
        multa = valor + 20 + atrasos * 0.50
        print('Valor com multa R$', multa)
