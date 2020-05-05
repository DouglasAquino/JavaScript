def verificaPositivo(valor):
     if valor > 0:
          return 'Positivo'
     else:
          return 'Negativo'

numero = int(input('Informe um numero: '))
print(numero, 'é', verificaPositivo(numero))
