num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
if num2 != 0:
    div = num1 / num2
    print('Resultado da divisão: {:.2f}'.format(div))
else:
    print('Não pode ser feita divisão por zero!')
